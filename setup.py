# -*- coding: UTF-8 -*-

from setuptools import setup
import os

read = lambda fname: open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-crudgenerator",
    version = "0.0.9",
    author = "Jonatan Alexis Anauati",
    author_email = "barakawins@gmail.com",
    description = ("A simple CRUD generator for django.",),
    license = "BSD",
    keywords = "web django crud generator automatic",
    packages=[\
        'djangocrudgenerator',
        'djangocrudgenerator/management',
        'djangocrudgenerator/management/commands',
        'djangocrudgenerator/templates',
        'djangocrudgenerator/templatetags',
        'djangocrudgenerator/config'
    ],
    package_data= {
        '':['*.html', '*.txt'],
    },
    long_description=read('README',),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
