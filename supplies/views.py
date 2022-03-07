from django.db.models import Q
from django.views import View
from django.shortcuts import render
from django.views.generic import ListView
from .forms import SuppliesSearchForm
from .models import (
    GroupSupplies,
    Supplies,
)
# Create your views here.


def homeView(request):
    template_name = 'supplies/home.html'
    queryset = None
    form = SuppliesSearchForm(request.POST or None)
    print(request.method)
    
    context = {'name': "Xin chao Device",
               'form': form,
               'supplies': queryset,
               }
    
    if request.method == 'POST':
        text_input = request.POST.get('text_input')
        queryset = Supplies.objects.filter(
            Q(code__icontains=text_input) |
            Q(name__icontains=text_input)
        ).distinct()
        print(queryset)
   
    
        context = {'name': "Xin chao Device",
                'form': form,
                'supplies': queryset,
        }
        
    return render(request, template_name, context)


def SearchForm(request):
    queryset=None
    template_name = 'supplies/result.html'
    
    context={}
    return (request, template_name, context)


class GroupSuppliesListView(ListView):
    mode = GroupSupplies
    template_name = 'supplies/list-groupsupplies.html'
    context_object_name = "groupsupplies"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = GroupSupplies.__name__
        return context

    def get_queryset(self):
        return GroupSupplies.objects.all()


class SuppliesListView(ListView):
    model = Supplies
    template_name = 'supplies/list-supplies.html'
    context_object_name = 'supplies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Supplies.__name__
        return context

    def get_queryset(self):
        return Supplies.objects.filter(group_supplies=self.kwargs['pk'])
