from django.shortcuts import render
from django.db import models

"""
class TabVendPro(models.Model):
    cd_Almoxarifado = models.IntegerField()
    cd_Grupo        = models.IntegerField()                                               
    cd_Produto      = models.IntegerField() 
    qt_Produto      = models.DecimalField(max_digits=15, decimal_places=2)
    vl_Transf       = models.DecimalField(max_digits=17, decimal_places=2)
    nr_Contrato     = models.IntegerField()
    tp_Fin          = models.CharField(max_length=2, blank=True, null=True) 
    cd_Modelo       = models.IntegerField()
    cd_Vendedor     = models.IntegerField()
    sg_Loja         = models.CharField(max_length=3, blank=True, null=True) 
    nr_Secao        = models.CharField(max_length=2, blank=True, null=True)  
    cd_Fornecedor   = models.IntegerField()
    cd_Subgrupo     = models.IntegerField()
    cd_Linha        = models.IntegerField()
    cd_Classe       = models.CharField(max_length=4, blank=True, null=True)  
    dt_Venda        = models.DateField(blank=True, null=True)
    cd_Marca        = models.IntegerField()
    cd_Cor          = models.IntegerField()
    vl_Desp_Fin     = models.DecimalField(max_digits=10, decimal_places=2)
    cd_Representante= models.IntegerField()
    vl_Garantia     = models.DecimalField(max_digits=15, decimal_places=2)
    cd_Trib         = models.CharField(max_length=5, blank=True, null=True)   
    dt_Cancel       = models.DateField(blank=True, null=True)
    cd_Stb          = models.CharField(max_length=1, blank=True, null=True)
    tp_Contrato     = models.IntegerField()
    no_Fornecedor   = models.CharField(max_length=45, blank=True, null=True)
    no_Vendedor     = models.CharField(max_length=30, blank=True, null=True)
    Fl_Embalada     = models.CharField(max_length=1, blank=True, null=True)    
    nr_Minuta       = models.IntegerField()
    fl_Tipo         = models.CharField(max_length=1, blank=True, null=True)
    No_Secao        = models.CharField(max_length=20, blank=True, null=True)
    No_Linha        = models.CharField(max_length=25, blank=True, null=True)
    Vl_Prod         = models.DecimalField(max_digits=15, decimal_places=2)
    Vl_Cont         = models.DecimalField(max_digits=15, decimal_places=2)
    vl_cubtot       = models.DecimalField(max_digits=15, decimal_places=2)
    vl_GarantiaDf   = models.DecimalField(max_digits=15, decimal_places=2)

    #cd_Chave_Sub (cd_Almoxarifado,cd_Subgrupo)   
    #cd_Chave_Cat (cd_Almoxarifado,cd_grupo, cd_Produto)   
    #cd_Chave_Con (sg_Loja,tp_Contrato,tp_Fin,nr_Contrato)
    #cd_Chave_Ven (sg_Loja,cd_Almoxarifado,cd_Vendedor)   

    class Meta:
        managed = False
        db_table = 'TabVendPro'
"""

