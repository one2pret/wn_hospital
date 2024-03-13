# -*- coding: utf-8 -*-
{
    'name': "Sistem Rumah Sakit",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "wawan",
    'website': "https://www.wawan.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    "data": [
        # "#security/ir.model.access.csv",
        #"views/views.xml",
        #"views/templates.xml",
        #"views/wn_hospital_wn_hospital_views.xml",
        "views/menu.xml",
        "views/hospital_patient_views.xml"
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
