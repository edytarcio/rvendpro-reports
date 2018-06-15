# filters.py
import django_filters
from .models import TabVendPro


class TabVendProFilter(django_filters.FilterSet):
  
  class Meta:
    model = TabVendPro
    fields = ['cd_almoxarifado', 'nr_contrato', 'dt_venda', 'no_descricao', 'nr_minuta', 'vl_cont']
    order_by = ['pk']
