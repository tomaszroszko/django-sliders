from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

#True if filebrwoser is installed
from sliders.managers import SliderManager, SliderPhotoManager

IS_FILEBROWSER = 'filebrowser' in settings.INSTALLED_APPS
if IS_FILEBROWSER:
    from filebrowser.fields import FileBrowseField


class Slider(models.Model):
    """
        Store information about slider
    """
    name = models.CharField(_('Name'), max_length=255)
    slug_name = models.SlugField(_('Slug'), max_length=255)
    is_active = models.BooleanField(_('Is active'), default=True)

    objects = SliderManager()

    class Meta:
        verbose_name = _('Slider')
        verbose_name_plural = _('Sliders')

    def __unicode__(self):
        return self.name


class SliderPhoto(models.Model):
    """
        Store sliders photos
    """
    slider = models.ForeignKey(Slider)
    if IS_FILEBROWSER:
        image = FileBrowseField("Image", max_length=255,
            extensions=('.jpg', '.png'))
    else:
        image = models.ImageField(upload_to='sliders/%Y/%m/%d')
    is_active = models.BooleanField(_('Is active'), default=True)
    active_from = models.DateTimeField(null=True, blank=True)
    active_to = models.DateTimeField(null=True, blank=True)
    order = models.IntegerField(_('Order'), default=0)

    objects = SliderPhotoManager()

    class Meta:
        verbose_name = _('Slider photo')
        verbose_name_plural = _('Slider photos')
        ordering = ('order',)

    def __unicode__(self):
        return self.image.url
