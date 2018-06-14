import django_tables2 as tables
from django_tables2.utils import A
from .models import TabVendPro

class TabVendProTable(tables.Table):
    cd_Almoxarifado = tables.LinkColumn('tabvendpro-detail', args=[A('pk')]) 
    nr_Contrato     = tables.LinkColumn('tabvendpro-detail', args=[A('pk')])
    dt_Venda        = tables.LinkColumn('tabvendpro-detail', args=[A('pk')])
    no_descricao    = tables.LinkColumn('tabvendpro-detail', args=[A('pk')])
    nr_Minuta       = tables.LinkColumn('tabvendpro-detail', args=[A('pk')])
    #Vl_Cont   
    
    class Meta:
        model = TabVendPro
        # here...
        fields = ('cd_Almoxarifado', 'nr_Contrato', 'dt_Venda', 'no_descricao', 'nr_Minuta', 'Vl_Cont')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "Nao foram encontrados registros com esses criterios..."

