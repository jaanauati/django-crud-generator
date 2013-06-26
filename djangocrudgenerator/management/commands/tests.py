# -*- coding: utf-8 -*-
from django.test import TestCase
from django import template
from django.utils.safestring import SafeText
from djangocrudgenerator.templatetags import generatortags
from djangocrudgenerator.management.commands.crudgen import ModelCRUDGenerator
from djangocrudgenerator.models import DjangoCRUDGeneratorTestModel

import os
import tempfile
import inspect
import itertools
import string
import djangocrudgenerator


__all__ = ('ModelCRUDGeneratorTestCase',)


class ModelCRUDGeneratorTestCase(TestCase):

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.settings= {
            "files": [
                {
                    "template": "only_for_testing_dont_override.txt",
                    "name": tempfile.mktemp()+'${appname}${modelname_lower}',
                    "override": True,
                },
                {
                    "template": "only_for_testing_dont_override.txt",
                    "name": tempfile.mktemp()+'${appname}${modelname_lower}',
                    "override": False,
                },
            ]
        }
        self.appname = 'djangocrudgenerator'
        self.model_class = DjangoCRUDGeneratorTestModel
        self.modelname = self.model_class.__name__
        self.modelname_lower = self.modelname.lower()
        self.application_path = os.path.dirname(djangocrudgenerator.__file__)
        self.template_name = 'only_for_testing_dont_override.txt'
        self.full_template_name = 'djangocrudgenerator/' + self.template_name
        self.tmpl_fullpath_alternative=os.path.join(
            self.application_path,
            "templates",
            self.template_name)
        self.rendered_template = u'%s.%s\n' % (self.appname, self.modelname)

    def __create_new_generator(self):
        args_spec = inspect.getargspec(ModelCRUDGenerator.__init__)
        self.assertEqual(len(args_spec.args), 4)
        self.assertEqual(args_spec.varargs, None)
        self.assertEqual(args_spec.keywords, None)
        return ModelCRUDGenerator(self.settings, self.appname, self.modelname)

    def test_create_new(self):
        generator = self.__create_new_generator()
        self.assertEqual(generator.__class__, ModelCRUDGenerator)
        self.assertEqual(generator.appname, self.appname)
        self.assertEqual(generator.modelname, self.modelname)
        self.assertEqual(generator.model, self.model_class)

    def test_get_model(self):
        get_model = ModelCRUDGenerator.get_model
        model_class = get_model(self.appname, self.modelname)
        self.assertEqual(model_class, self.model_class)

    def test_get_crungen_dir(self):
        get_crudgen_dir = ModelCRUDGenerator.get_crudgen_dir
        cg_dir = get_crudgen_dir()
        self.assertEqual(cg_dir, self.application_path)
        self.assertTrue(os.path.isdir(cg_dir))

    def test_gen_template_name(self):
        gen_template_name = ModelCRUDGenerator.gen_template_name
        s = gen_template_name(self.template_name)
        self.assertEqual(s, 'djangocrudgenerator/' + self.template_name)

    def test_get_template(self):
        get_template = ModelCRUDGenerator.get_template
        tmpl = get_template(
            self.full_template_name,
            self.tmpl_fullpath_alternative)
        self.assertEqual(tmpl.__class__, template.Template)

    def test_render_template(self):
        render_template = ModelCRUDGenerator.render_template
        context = {'appname': self.appname, 'modelname': self.modelname}
        res = render_template(self.template_name, context)
        self.assertTrue(res.__class__ == SafeText)
        self.assertEqual(unicode(res), self.rendered_template)

    def test_generate_files(self):
        generator = self.__create_new_generator()
        results = generator.generate_files()
        self.assertEqual(len(results['backup']), 0)
        for f in self.settings['files']:
            fname = string.Template(f['name']).substitute(self.__dict__)
            self.assertTrue(fname in results['generated'])
            self.assertEqual(file(fname).read(), self.rendered_template)
        for fname in itertools.chain(results['generated'], results['backup']):
            os.remove(fname)
