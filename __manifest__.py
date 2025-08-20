{
    'name': 'EAUT Career Center',
    'version': '1.0',
    'summary': 'Quản lý thông tin và hoạt động của sinh viên liên quan đến việc làm',
    'description': """
        EAUT Career Center:
        - Quản lý Sinh viên
        - Quản lý thông tin sinh viên (mã sinh viên, email...)
        - Theo dõi quá trình hoạt động của sinh viên, hướng đến mục tiêu mọi sinh viên đều có việc làm sau khi tốt nghiệp.
        - Tích hợp với các module CRM và Event để quản lý sự kiện Ngày hội việc làm.
    """,
    'category': 'EAUT',
    'author': 'EAUT',
    'website': '',
    'depends': [
        'base',
        'crm',
        'event',
        'mail',
        'calendar',
        'website_slides',
        'board',
    ],
    'data': [
        # 'security/security.xml',
        'views/eaut_career_center_student_views.xml',
        'views/eaut_career_center_employer_views.xml',
        'views/eaut_career_center_faculty_views.xml',
        'views/eaut_career_center_program_views.xml',
        'views/eaut_career_center_major_views.xml',
        'views/eaut_career_center_support_team_views.xml',
        'views/eaut_career_center_stage_views.xml',
        'views/eaut_career_center_tag_views.xml',
        'views/eaut_career_center_report_views.xml',
        'views/eaut_career_center_mou_contract_views.xml',
        'views/eaut_career_center_mou_scope_views.xml',
        'views/eaut_career_center_employer_industry_views.xml',
        # "views/dashboard.xml",

        'views/eaut_career_center_menus.xml',

        'security/eaut_career_center_security.xml',

        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend': [
            'eaut_career_center/static/src/css/student_view.css'
        ],
    },
    'installable': True,
    'application': True,
    'icon': '/eaut_career_center/static/description/icon.png',
    'license': 'LGPL-3',
}
