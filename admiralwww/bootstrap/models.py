# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Params(models.Model):
    key = models.CharField(max_length=50, db_index=True, verbose_name=_('Name'))    
    value = models.TextField()
    hint = models.CharField(max_length=255)
    class Meta:
        ordering = ['key']
        verbose_name = _("Params")
        verbose_name_plural = _("Paramss")
               

class Measure(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name=_('Name'))
    def __unicode__(self):
        return self.name    
    class Meta:
        ordering = ['name']  
        verbose_name = _("Measure")
        verbose_name_plural = _("Measures")


class Nds(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name=_('Name'))
    value = models.IntegerField(verbose_name=_('Value'), default=0)
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['name']
        verbose_name = _("Nds")
        verbose_name_plural = _("Ndses")

    
class PortServicie(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name=_('Name'))
    measure = models.ForeignKey(Measure, verbose_name=_('Measure'), on_delete=models.PROTECT)
    nds = models.ForeignKey(Nds, verbose_name=_('Nds'), on_delete=models.PROTECT)
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['name']
        verbose_name = _("PortServicie")
        verbose_name_plural = _("PortServicies")
    
    
class PortRate(models.Model):
    port_servicie = models.ForeignKey(PortServicie, verbose_name=_('Port servicie'), on_delete=models.PROTECT)
    not_dangerous_20 = models.DecimalField(verbose_name=_('Not Dangerous 20'), max_digits=8, decimal_places=2)    
    not_dangerous_40 = models.DecimalField(verbose_name=_('Not Dangerous 40'), max_digits=8, decimal_places=2)
    dangerous_20 = models.DecimalField(verbose_name=_('Dangerous 20'), max_digits=8, decimal_places=2)
    dangerous_40 = models.DecimalField(verbose_name=_('Dangerous 40'), max_digits=8, decimal_places=2)
    ref_40 = models.DecimalField(verbose_name=_('RFH 40'), max_digits=8, decimal_places=2)
    sort_order = models.IntegerField(verbose_name=_('Sort order'), default=100)
    def __unicode__(self):
        return u'%s' % self.port_servicie
    class Meta:
        ordering = ['sort_order']
        verbose_name = _("PortRate")
        verbose_name_plural = _("PortRates")