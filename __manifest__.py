# -*- coding: utf-8 -*-
{
    'name': "My Asset",

    'summary': """
       Test Coding Odoo MNC Odoo14""",

    'description': """
        Test Coding Odoo MNC Odoo14
    """,

    'author': "Ahmad Yulian Dinata",
    'website': "https://www.linkedin.com/in/ahmaddyd/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/my_asset_view.xml',
        'views/menu.xml',
        'views/project_task_inherit.xml',
        'report/report.xml',
        'report/report_my_asset.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
