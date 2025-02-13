{
    'name': "Task Priority",
    'version': '1.0',
    'depends': ['project'],
    'author': "Guillaume Villers",
    'category': '',
    'description': """
    Module pour ajouter une priorité sur les tâches
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        "views/complexity_views.xml",
        "views/importance_views.xml",
        "views/project_task_views.xml",
        "views/priority_menus.xml",
    ],
    # data files containing optionally loaded demonstration data
    'demo': [

    ],
    'application': False,
}