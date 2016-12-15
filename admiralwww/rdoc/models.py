# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime
from rdoc.util import attachment_path
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.encoding import force_unicode

class DocCategory(MPTTModel):
    """
    Doc category    
    """
    title = models.CharField(
        _('Title'),
        help_text=_('Document category title'),
        max_length=255,
        )
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    slug = models.SlugField()
    
    def __unicode__(self):
        return u"%s" % self.title
    
    class MPTTMeta:
        order_insertion_by = ['title']
    
    class Meta:
        verbose_name = _('document category')
        verbose_name_plural = _('document categories')
        ordering = ('title',)   

class Doc(models.Model):
    """
    Docs for site
    """

    title = models.CharField(
        _('Title'),
        help_text=_('Document title'),
        max_length=255,
        )

    description = models.TextField(
        _('Description'),
        help_text=_('Document description'),        
        blank=True,
        null=True,
        )
    
    issue_date = models.DateField(
        _('Date'),
        help_text=_('Document date'),
        blank=True,
        null=True,
        )
    
    attachment = models.FileField(
        _('Attachment'),
        help_text=_('Document attachment'),
        upload_to=attachment_path,
    )
    
    pub_date = models.DateField(
        _('Modification date'),
        help_text=_('Document modification date'),
        default=datetime.date.today(),
        )    
        
    doc_category = models.ForeignKey(DocCategory, verbose_name=_('document category'))
    
    def __unicode__(self):
        return u"%s" % self.title
    
    def get_info(self):
        info =  '%s: %s\n' % (force_unicode(_('Title')), self.title)
        if self.desciption:
            info += '%s: %s\n' % (force_unicode(_('Description')), self.desciption)
        if self.issue_date:    
            info += '%s: %s\n' % (force_unicode(_('Date')), self.issue_date.strftime('%d.%m.%Y'))  
        info += '%s: %s\n' % ('id', self.id)
        return info

    class Meta:
        verbose_name = _('document entry')
        verbose_name_plural = _('document entries')
        ordering = ('-issue_date', 'title',)                
