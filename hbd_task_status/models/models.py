# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from openerp import models, fields, api, _


class ProjectTaskReport(models.TransientModel):
    _name = "project.task.report"

    owner_id = fields.Many2one(comodel_name="res.users", string="Owner")
    project_id = fields.Many2one("project.project", string="Project")
    open_tasks = fields.Integer(string="Open Tasks")
    delay_tasks = fields.Integer(string="Delay Tasks")
    finish_month = fields.Integer(string="Finish Month")
    finish_week = fields.Integer(string="Finish Week")

    @api.multi
    def action_generate_report(self):
        ids = self._action_generate_report()

        return {
            "name": _("Project Tasks Report"),
            "type": "ir.actions.act_window",
            "res_model": "project.task.report",
            "view_mode": "tree",
            "view_type": "form",
            "domain": [("id", "in", ids)],
            "views": [
                [False, "tree"],
            ],
            "context": {"search_default_group_by_owner_id": True},
        }

    @api.multi
    def _action_generate_report(self):
        day = 1
        ids = []

        domain = [
            ("user_id", "!=", ""),
        ]
        self.env["project.task.report"].search([]).unlink()
        project_ids = self.env["project.project"].search(domain)
        this_month = datetime.today().replace(day=day)
        this_week = (datetime.today() - timedelta(days=7)).date()

        for project_id in project_ids:
            open_tasks = project_id.task_ids.filtered(
                lambda r: not r.stage_id.closed and r.user_id == r.project_id.user_id
            )
            delay_tasks = project_id.task_ids.filtered(lambda r: r.date_deadline).filtered(
                lambda r: fields.Datetime.from_string(r.date_deadline) < datetime.now()
            )

            finish_month = project_id.task_ids.filtered(
                lambda r: r.stage_id.closed and fields.Datetime.from_string(r.date_end) >= this_month
            )
            this_week = project_id.task_ids.filtered(
                lambda r: r.stage_id.closed and fields.Datetime.from_string(r.date_end) >= this_week
            )

            ids.append(
                self.create(
                    {
                        "owner_id": project_id.user_id.id,
                        "project_id": project_id.id,
                        "open_tasks": len(open_tasks),
                        "delay_tasks": len(delay_tasks),
                        "finish_month": len(finish_month),
                        "finish_week": len(this_week),
                    }
                ).id
            )
        return ids
