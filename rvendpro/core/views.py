from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query_utils import Q
from django_tables2 import RequestConfig
#from braces.views import LoginRequiredMixin, GroupRequiredMixin
from .tables import TabVendProTable
from .filters import TabVendProFilter
from .utils import PagedFilteredTableView
from .models import TabVendPro
from .forms import TabVendProFormHelper

# here...
#class TabVendProView(LoginRequiredMixin, GroupRequiredMixin, PagedFilteredTableView):
class TabVendProView(PagedFilteredTableView):
    model = TabVendPro
    template_name = 'tabvendpro.html'
    context_object_name = 'tabvendpro'
    ordering = ['-id']
    # here...
    #group_required = u'company-user'
    table_class = TabVendProTable
    filter_class = TabVendProFilter
    formhelper_class = TabVendProFormHelper

    def get_queryset(self):
        qs = super(TabVendProView, self).get_queryset()
        return qs
    
    def post(self, request, *args, **kwargs):
        return PagedFilteredTableView.as_view()(request)

    def get_context_data(self, **kwargs):
        context = super(TabVendProView, self).get_context_data(**kwargs)
        # here...
        context['nav_tabvendpro'] = True
        search_query = self.get_queryset()
        table = TabVendProTable(search_query)
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context

# here... Creating a separate class; Refactor Details Page Strategy
# tabvendpro-detail
def venda_detail(request, *args, **kwargs):
    print ('args...:', args)
    print ('kargs...:', kwargs)
    #return render(request, 'tabvendpro_detail.html', {'data': {}})
    return render(request, 'tabvendpro_detail.html', {'data': args})
