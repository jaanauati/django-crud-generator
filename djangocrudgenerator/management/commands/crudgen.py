# -*- coding: UTF-8 -*-

import os
import time
from string import Template

from django.core.management.base import BaseCommand, CommandError
from django.template import loader, Context
from django.template.loader import get_template, select_template
from django import template

from djangocrudgenerator.config.settings import DJANGOCRUDGENERATOR_SETTINGS
from django.conf import settings
try:
    DJANGOCRUDGENERATOR_SETTINGS = settings.DJANGOCRUDGENERATOR_SETTINGS
except AttributeError:
    pass
import djangocrudgenerator

class ModelCRUDGenerator(object):
    """ Generator helper."""
    def __init__(self, appname, modelname):
        """Initializes an ModelCRUDGenerator instance.
            - appname: the target application.
            - modelname: the target model.
            If either the application is invalid or the model `modelname` does 
            not exist inside the `models.py` file of the application, an  
            `CommandError` will be raised.
        """
        model = self.get_model(appname, modelname)
        if not model:
            raise CommandError("Invalid parameters: %s %s" % \
                (appname, modelname))
        self.model=model
        self.appname=appname
        self.modelname=modelname
    @classmethod
    def get_model(cObj, appname, modelname):
        """ Returns the`modelname` class object. If either the application or
            the model is invalid, then `None` is returned.
        """
        try:
            module=__import__(appname)
            model = getattr(getattr(module,'models'), modelname)
            return model
        except Exception, ex:
            return None
    @classmethod
    def get_crudgen_dir(cObj):
        """ Returns the installation directory of djangocrudgenerator. """
        return os.path.dirname(djangocrudgenerator.__file__)
    @classmethod
    def gen_template_name(cObj, name):
        return 'djangocrudgenerator/'+name
    @classmethod
    def get_template(cObj, templ_name, alternative_tmpl):
        """ Finds the given template, the user can override the 
            djangocrudgenerator self-contained template via the templates 
            directories ("templates/djangocrudgenerator").
            An Template instance will be returned.
        """
        return select_template([cObj.gen_template_name(templ_name),alternative_tmpl])
    @classmethod
    def render_template(cObj, template_name, context_data):
        """ This method renders the template with the given context data and returns
            the result."""
        templ_fullpath_alternative="%s/%s" % (cObj.get_crudgen_dir()+
                                                "/templates",
                                              template_name)
        template= cObj.get_template(
            template_name,
            templ_fullpath_alternative)
        return template.render(Context(context_data))
    @classmethod
    def create_dirs(cObj, pathname):
        head,tail=os.path.split(pathname)
        if head:
            cObj.create_dirs(head)
        if tail:
            try:
                os.mkdir(os.path.join(head,tail))
            except Exception, ex:
                if ex[0] != 17:
                    raise ex
    def generate_files(self):
        settings = DJANGOCRUDGENERATOR_SETTINGS
        try:
            for f in settings['files']:
                template = f['template']
                context_data={
                   'modelname':self.modelname,
                   'modelname_lower':self.modelname.lower(),
                   'appname':self.appname,
                   'template':template
                }
                raw_name = f['name']
                override = f.get('override',False)
                backup = f.get('backup',bool(override))
                full_name=Template(raw_name).substitute(**context_data)
                self.create_dirs(os.path.split(full_name)[0])
                contents=self.render_template(template, context_data)
                if backup:
                    backup_name = full_name+"."+str(int(time.time()))
                    try:
                        srcfile=file(full_name)
                        backupfile=file(backup_name,"w")
                        backupfile.write(srcfile.read())
                        backupfile.close()
                        srcfile.close()
                    except IOError:
                        pass
                    else:
                        print("Created Backup: %s" % backup_name)
                if override:
                    flags="w"
                else:
                    flags="a+"
                output=file(full_name, flags)
                output.write(contents)
                output.close()
                print("Generated: %s" % full_name)
        except KeyError:
            raise CommandError("Invalid configuration.")

class Command(BaseCommand):
    args = '<app_name model_name ...>'
    help = 'Generates a C.R.U.D. for the selected application model.'
    def handle(self, *args, **options):
        try:
            app_name = args[0]
            model_name=args[1]
        except:
            raise CommandError("Invalid paramters.")
        ModelCRUDGenerator(app_name, model_name).generate_files()
        self.stdout.write('%s.%s CRUD successfully generated.\n' % (app_name, model_name))
