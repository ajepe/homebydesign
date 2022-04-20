# -*- coding: utf-8 -*-
{
    "name": "hbd_task_status",
    "summary": """hbd_task_status""",
    "description": """
        Long description of module's purpose
    """,
    "author": "Babatope Ajepe",
    "website": "http://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base", "project", "portal_project"],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/views.xml",
        "views/templates.xml",
        "data/data.xml",
    ],
}
