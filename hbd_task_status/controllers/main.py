# -*- coding: utf-8 -*-
import logging
import werkzeug

from openerp import SUPERUSER_ID
from openerp import http
from openerp import tools
from openerp.http import request
from openerp.tools.translate import _
from openerp.addons.website.models.website import slug
from openerp.addons.web.controllers.main import login_redirect


class TasksReport(http.Controller):
    """."""

    def _get_tasks_report_data(self):
        tasks = []
        records = request.env["project.task"].search([])
        return tasks

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

        values = self._get_tasks_report_data()
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", values)
        values = {}
        return request.website.render("hbd_task_status.tasks", values)
