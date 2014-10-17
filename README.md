<b> INSTALL:

1. Just run:
```
$ pip install -e git+git@github.com:jaanauati/django-crud-generator.git@master#egg=django-crud-generator
```

<b> USAGE:
1.  First, you must add the 'djangocrudgenerator' application into the settings file:
```
INSTALLED_APPS = (
    ...
    'yourwebapp',
    'djangocrudgenerator',
    ...
)
```
1. Supposing that you have created an application named 'yourwebapp', add the following to the project urlconf file (urls.py):
```
urlpatterns = patterns('',
    ...
    url(r'^yourwebapp/', include('yourwebapp.urls',namespace="yourwebapp")),
    ...
)
```
It's also necessary to include the templates directory of your application in the settings file:
```
TEMPLATE_DIRS = (
    ...
    'path/to/yourwebapp/templates',
)
```
1. Add an example model to the 'yourwebapp' app:
```
#models.py
class YourModel(models.Model):
    name=models.CharField(max_length=30)
    ...
    def __str__(self):
        return self.name
```
and then synchronize your database (syncdb, south, evolution...).
1. Now you can use the crud generator. For example, if you want generate a CRUD for the 'YourModel' model, you must run the following command:
```
$ python manage.py crudgen yourwebapp YourModel
```
1. To test the generated CRUD, first you must run the django development server:
```
$ python manage.py runserver
```
and then, go to http://localhost:8000/yourwebapp/yourmodel/list/page1/ in your web browser.

Enjoy!
