from django.views.generic import ListView
#from braces.views import LoginRequiredMixin, GroupRequiredMixin
from django_tables2 import RequestConfig
from .models import TabVendPro
from .tables import TabVendProTable


class TabVendProListView(ListView):
  model = TabVendPro 
  template_name = 'tabvendpro.html'
  context_object_name = 'customer'
  #ordering = ['id']
  #group_required = u'company-user'

  def get_context_data(self, **kwargs):
    context = super(TabVendProListView, self).get_context_data(**kwargs)
    #context['nav_customer'] = True
    #table = TabVendProTable(TabVendPro.objects.filter(self.kwargs['no_secao']))
    table = TabVendProTable(TabVendPro.objects.all())
    RequestConfig(self.request, paginate={'per_page': 20}).configure(table)
    context['table'] = table
    return context
