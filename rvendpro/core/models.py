from django.shortcuts import render
from django.db import models

class TabVendPro(models.Model):
    cd_almoxarifado = models.IntegerField()
    nr_contrato     = models.IntegerField()
    dt_venda        = models.DateField(blank=True, null=True)
    no_descricao    = models.CharField(max_length=45, blank=True, null=True)
    nr_minuta       = models.IntegerField()
    vl_cont         = models.DecimalField(max_digits=15, decimal_places=2)


    class Meta:
        db_table = "tabvendpro"
        verbose_name = 'Tabvendpro'
        verbose_name_plural = 'TabVendPros'
        ordering = ['-id']
