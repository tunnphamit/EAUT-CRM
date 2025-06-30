{
    'name': 'EAUT CRM',
    'version': '1.0',
    'summary': 'Quản lý thông tin và hoạt động của sinh viên liên quan đến Ngày hội việc làm',
    'description': """
        EAUT CRM:
        - Quản lý Sinh viên
        - Quản lý thông tin sinh viên (mã sinh viên, email...)
        - Theo dõi quá trình hoạt động của sinh viên, hướng đến mục tiêu mọi sinh viên đều có việc làm sau khi tốt nghiệp.
        - Tích hợp với các module CRM và Event để quản lý sự kiện Ngày hội việc làm.
    """,
    'category': 'CRM',
    'author': 'Your Name',
    'website': 'https://yourcompany.com',
    'depends': ['base', 'crm', 'event'],
    'data': [
        # 'security/security.xml',
        'views/student_views.xml',
        'views/eaut_crm_menus.xml',
        
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'icon': '/eaut_crm/static/description/icon.png',
    'license': 'LGPL-3',
}
