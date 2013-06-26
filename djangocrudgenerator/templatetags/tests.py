# -*- coding: utf-8 -*-

from django.test import TestCase
from django import template
from djangocrudgenerator.templatetags import generatortags

__all__ = ('GeneratorTagsTestCase',)


class GeneratorTagsTestCase(TestCase):

    def test_gen_url_tag(self):
        self.assertEqual(
            generatortags.gen_url_tag("first", "second", "last", arg=1),
            '{% url "first:second:last" arg="1" %}')
        with self.assertRaises(template.TemplateSyntaxError):
            generatortags.gen_url_tag(arg=1)

    def __simple_func_test(self, fcn, ret):
        self.assertEqual(fcn(), ret)
        with self.assertRaises(TypeError):
            fcn(1)

    def test_start_tag(self):
        self.__simple_func_test(generatortags.start_tag, '{%')

    def test_end_tag(self):
        self.__simple_func_test(generatortags.end_tag, '%}')

    def test_start_var(self):
        self.__simple_func_test(generatortags.start_var, '{{')

    def test_start_var(self):
        self.__simple_func_test(generatortags.end_var, '}}')

    def test_start_comment(self):
        self.__simple_func_test(generatortags.start_comment, '{#')

    def test_end_comment(self):
        self.__simple_func_test(generatortags.end_comment, '#}')
