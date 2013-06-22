# -*- coding: utf-8 -*-


"""
Configuration file of the generator.
Important note: The groups 'appname' and 'modelname' will be expanded to
the application and model name.
"""
DJANGOCRUDGENERATOR_SETTINGS = {
    "files": [
        {
            "template": "model_form.html",
            "name": "${appname}/templates/${appname}/" +
                    "${modelname_lower}_form.html",
            "override": True,
        },
        {
            "template": "model_confirm_delete.html",
            "name": "${appname}/templates/${appname}/" +
                    "${modelname_lower}_confirm_delete.html",
            "override": True,
        },
        {
            "template": "model_list.html",
            "name": "${appname}/templates/${appname}/" +
                    "${modelname_lower}_list.html",
            "override": True,
        },
        {
            "template": "views.py",
            "name": "${appname}/views.py",
            "override": False,
        },
        {
            "template": "urls.py",
            "name": "${appname}/urls.py",
            "override": False,
        },
    ]
}
