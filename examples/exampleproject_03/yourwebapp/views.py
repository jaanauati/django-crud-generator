# Create your views here.
#crudgenerator auto-generated code.
#crudgenetaror date: 15th January 2012 09:27
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from models import YourModel
from yourwebapp.forms import YourModelModelForm


class YourModelListView(ListView):
    model=YourModel
    paginate_by=20

class YourModelDeleteView(DeleteView):
    model=YourModel
    def get_success_url(self):
        return reverse("yourwebapp:yourmodel:list", args=(1,))

class YourModelCreateView(CreateView):
    model=YourModel
    form_class=YourModelModelForm
    def get_success_url(self):
        return reverse("yourwebapp:yourmodel:list", args=(1,))

class YourModelUpdateView(UpdateView):
    model=YourModel
    def get_success_url(self):
        return reverse("yourwebapp:yourmodel:list", args=(1,))
