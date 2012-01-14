# -*- coding: UTF-8 -*-
"""
Configuration file of the generator.
Important note: The groups 'appname' and 'modelname' will be expanded to 
the application and model name.

"""
DJANGOCRUDGENERATOR_SETTINGS = {
    "files" : [\
        {   "template":"model_form.html",
            "name": "(?<appname>[^_]+)/templates/(?<appname>[^_]+)/(?<modelname>[^_]+)_form.html",
            "override":True,
        },
        {   "template":"model_confirm_delete.html",
            "name": "(?<appname>[^_]+)/templates/(?<appname>[^_]+)/(?<modelname>[^_]+)_confirm_delete.html",
            "override":True,
        },
        {   "template":"model_list.html",
            "name": "(?<appname>[^_]+)/templates/(?<appname>[^_]+)/(?<modelname>[^_]+)_list.html",
            "override":True,
        },
        {   "template":"views.py",
            "name": "(?<appname>[^_]+)/views.html",
            "override":False,
        },
        {   "template":"urls.py",
            "name": "(?<appname>[^_]+)/views.html",
            "override":False,
        },
    ]
}
