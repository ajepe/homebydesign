# -*- coding: utf-8 -*-

import json
import logging
import werkzeug
import werkzeug.wrappers
from itertools import groupby


from openerp import SUPERUSER_ID
from openerp import http
from openerp.http import request


class TasksReport(http.Controller):
    """."""

    def _get_tasks_report_data(self):
        tasks = []
        report = request.env["project.task.report"].sudo(SUPERUSER_ID)
        ids = report._action_generate_report()

        data = [
            {
                "state": rec.state,
                "project": rec.project_id.name,
                "project_id": rec.project_id.id,
                "open_tasks": rec.open_tasks,
                "finish_month": rec.finish_month,
                "delay_tasks": rec.delay_tasks,
                "finish_week": rec.finish_week,
                "owner_id": rec.owner_id.id,
                "owner_name": rec.owner_id.name,
                "image": rec.image,
            }
            for rec in report.browse(ids)
        ]
        data = sorted(data, key=lambda rec: rec.get("owner_name"))
        group_data = groupby(data, key=lambda rec: rec.get("owner_name"))
        for key, values in group_data:
            tasks.append({key: list(values)})
        return werkzeug.wrappers.Response(
            status=200,
            content_type="application/json; charset=utf-8",
            response=json.dumps(tasks),
        )

    @http.route(
        ["/api-tasks-status"],
        type="http",
        auth="public",
        website=True,
    )
    def api_tasks_status(self, **post):
        cr, uid, context, pool = (
            request.cr,
            request.uid,
            request.context,
            request.registry,
        )

        values = self._get_tasks_report_data()
        return values

    @http.route(
        ["/tasks"],
        type="http",
        auth="public",
        website=True,
    )
    def tasks(self, **post):
        cr, uid, context, pool = (
            request.cr,
            request.uid,
            request.context,
            request.registry,
        )

        return request.render("hbd_task_status.tasks", {})
