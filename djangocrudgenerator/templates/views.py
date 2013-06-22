# -*- coding: utf-8 -*-

#crudgenerator auto-generated code.
#crudgenetaror date: {% now  "jS F Y H:i"  %}


from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from models import {{modelname}}


__all__ = ('{{modelname}}ListView', '{{modelname}}UpdateView',
           '{{modelname}}CreateView', '{{modelname}}DeleteView')


class {{modelname}}ListView(ListView):
    model = {{modelname}}
    paginate_by = 20


class {{modelname}}DeleteView(DeleteView):
    model = {{modelname}}

    def get_success_url(self):
        return reverse("{{appname|lower}}:{{modelname|lower}}:list", args=(1,))


class {{modelname}}CreateView(CreateView):
    model = {{modelname}}

    def get_success_url(self):
        return reverse("{{appname|lower}}:{{modelname|lower}}:list", args=(1,))


class {{modelname}}UpdateView(UpdateView):
    model = {{modelname}}

    def get_success_url(self):
        return reverse("{{appname|lower}}:{{modelname|lower}}:list", args=(1,))
