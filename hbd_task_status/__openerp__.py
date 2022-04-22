# -*- coding: utf-8 -*-
{
    "name": "hbd_task_status",
    "summary": """hbd_task_status""",
    "description": """
        Long description of module's purpose
    """,
    "author": "Babatope Ajepe",
    "website": "http://www.yourcompany.com",
    "category": "Uncategorized",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": [
        "base",
        "website",
        "project",
        "sale_service",
        "project_issue",
        "portal_project",
        "web_tree_image",
    ],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/views.xml",
        "views/templates.xml",
        "data/data.xml",
    ],
}
