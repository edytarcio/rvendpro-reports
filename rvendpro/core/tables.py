import django_tables2 as tables
from django_tables2.utils import A
from .models import TabVendPro

class TabVendProTable(tables.Table):
    cd_almoxarifado = tables.LinkColumn('venda_detail') 
    nr_contrato     = tables.LinkColumn('venda_detail')
    dt_venda        = tables.LinkColumn('venda_detail')
    no_descricao    = tables.LinkColumn('venda_detail')
    nr_minuta       = tables.LinkColumn('venda_detail')
    cd_almoxarifado = tables.LinkColumn('venda_detail') 
    vl_cont = tables.LinkColumn('venda_detail') 
    #cd_almoxarifado = tables.LinkColumn('venda_detail', text='static text', args=[A('pk')], empty_values=()) 
    
    class Meta:
        model = TabVendPro
        # here...
        #fields = ('cd_almoxarifado', 'nr_contrato', 'dt_venda', 'no_descricao', 'nr_minuta', 'vl_cont')
        fields = ('nr_contrato', 'dt_venda', 'no_descricao', 'nr_minuta', 'vl_cont')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "Nao foram encontrados registros com esses criterios..."

