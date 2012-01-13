from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from models import Modelname


class ModelnameListView(ListView):
    model=Modelname
    template_name="{{appname|lower}}/{{modelname|lower}}_list.html"

class ModelnameDeleteView(DeleteView):
    model=Modelname
    template_name="{{appname|lower}}/{{modelname|lower}}_confirm_delete.html"
    def get_success_url(self):
        return reverse("appname:modelname:list", args=(1,))

class ModelnameCreateView(CreateView):
    model=Modelname
    template_name="{{appname|lower}}/{{modelname|lower}}_form.html"
    def get_success_url(self):
        return reverse("appname:modelname:list", args=(1,))

class ModelnameUpdateView(UpdateView):
    model=Modelname
    template_name="{{appname|lower}}/{{modelname|lower}}_form.html"
    def get_success_url(self):
        return reverse("appname:modelname:list", args=(1,))

