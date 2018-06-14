# filters.py
import django_filters
from .models import TabVendPro


class TabVendProFilter(django_filters.FilterSet):
  
  class Meta:
    model = TabVendPro
    fields = ['cd_Almoxarifado', 'nr_Contrato', 'dt_Venda', 'no_descricao', 'nr_Minuta', 'Vl_Cont']
    order_by = ['pk']
