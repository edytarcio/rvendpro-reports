from django.shortcuts import render
from django.db import models

class TabVendPro(models.Model):
    cd_Almoxarifado = models.IntegerField()
    nr_Contrato     = models.IntegerField()
    dt_Venda        = models.DateField(blank=True, null=True)
    no_descricao    = models.CharField(max_length=45, blank=True, null=True)
    nr_Minuta       = models.IntegerField()
    Vl_Cont         = models.DecimalField(max_digits=15, decimal_places=2)


    class Meta:
        verbose_name = 'Tabvendpro'
        verbose_name_plural = 'Tabvendpros'
        ordering = ['-id']
