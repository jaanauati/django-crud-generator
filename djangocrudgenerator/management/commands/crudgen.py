# -*- coding: UTF-8 -*-

from django.core.management.base import BaseCommand, CommandError
from django import template
from django.template import loader, Context
import os
import djangocrudgenerator

class ModelCRUDGenerator(object):
    def __init__(self, appname, modelname):
        model = self.get_model(appname, modelname)
        if not model:
            raise CommandError("Invalid parameters: %s %s" % \
                (appname, modelname))
        self.model=model
        self.appname=appname
        self.modelname=modelname
    def get_app_dir(self):
        module=__import__(self.appname)
        if module:
            return os.path.dirname(module.__file__)
        return None
    @classmethod
    def get_model(cObj, appname, modelname):
        try:
            module=__import__(appname)
            model = getattr(getattr(module,'models'), modelname)
            return model
        except Exception, ex:
            return None
    @classmethod
    def get_crudgen_dir(cObj):
        """ Returns the application installation directory. """
        return os.path.dirname(djangocrudgenerator.__file__)
    @classmethod
    def render_template(cObj, template_name, context_data):
        templ_fullpath="%s/%s" % (cObj.get_crudgen_dir()+"/templates",
                                  template_name)
        return loader.get_template(templ_fullpath).render(
                        Context(context_data))
    def get_app_templates_dirs(self):
        base=self.get_app_dir()+"/templates"
        app=base+"/"+self.appname
        return (base, app)
    def create_directories(self):
        templates_base_dirs=self.get_app_templates_dirs()
        for dir in templates_base_dirs:
            try:
                os.mkdir(dir)
            except Exception, ex:
                if ex[0] != 17:
                    raise ex
    def create_templates(self):
        sufixes=['form', 'list', 'confirm_delete']
        for sufix in sufixes:
            templ_templ_name="model_%s.html" % sufix
            templ_name="%s_%s.html" % (self.modelname.lower(), sufix)
            templ_templ_fullpath="%s/%s" % (
                    self.get_crudgen_dir()+"/templates",
                    templ_templ_name)
            templ_fullpath="%s/%s" % (self.get_app_templates_dirs()[-1],
                                templ_name)

            c = Context({
                'modelname':self.modelname,
                'appname':self.appname,
                'template':sufix,
            }) 
            out = file(templ_fullpath,"w")
            currentTempl=loader.get_template(templ_templ_fullpath).render(c)
            out.write(currentTempl)
            out.close()
    def create_views(self):
        """ This method does the following:
            - Generates the python views code.
            - Inserts the generated code into the 'views.py' file.
        """
        templ_name="views.py" 
        cdata={'modelname':self.modelname,
               'appname':self.appname,
               'template':templ_name}
        gendata=self.render_template('views.py', cdata)
        appviews_file=self.get_app_dir()+"/views.py"
        output=file(appviews_file, "a+")
        output.write(gendata)
        output.close()
    def create_urls(self):
        """ This method does the following:
            - Generates the urlconfs.
            - Inserts the generated urls into the `urlpatterns` variable.
        """
        templ_name="urls.py" 
        cdata={'modelname':self.modelname,
               'appname':self.appname,
               'template':templ_name}
        gendata=self.render_template('urls.py', cdata)
        appurls_file=self.get_app_dir()+"/urls.py"
        output=file(appurls_file, "a+")
        output.write(gendata)
        output.close()
class Command(BaseCommand):
    args = '<app_name model_name ...>'
    help = 'Generates a C.R.U.D. for the selected application model.'
    def handle(self, *args, **options):
        try:
            app_name = args[0]
            model_name=args[1]
        except:
            raise CommandError("Invalid paramters.")
        generator=ModelCRUDGenerator(app_name, model_name)
        generator.create_directories()
        generator.create_templates()
        generator.create_views()
        generator.create_urls()
        self.stdout.write('%s.%s CRUD succesfully created.\n' % (app_name, model_name))
