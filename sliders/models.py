from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

#True if filebrwoser is installed
from sliders.managers import SliderManager, SliderPhotoManager
from sliders import consts

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
            extensions=('.jpg', '.png'), null=True, blank=True)
    else:
        image = models.ImageField(upload_to='sliders/%Y/%m/%d', null=True,
            blank=True)

    video = models.CharField(_('Video'), max_length=255, null=True, blank=True)

    title = models.CharField(_('Title'), max_length=255, null=True,
                             blank=True)
    description = models.TextField(_('Description'), null=True, blank=True)
    links_to = models.CharField(_('Links To'), null=True, blank=True,
                                max_length=255)

    content_type = models.ForeignKey(ContentType, null=True, blank=True,
        limit_choices_to=consts.SLIDE_CONTENT_TYPES,
        related_name='content_type')
    object_id = models.IntegerField(_('Object ID'), null=True, blank=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    is_active = models.BooleanField(_('Is active'), default=True)
    active_from = models.DateTimeField(null=True, blank=True)
    active_to = models.DateTimeField(null=True, blank=True)
    order = models.IntegerField(_('Order'), default=0)
    css_class = models.CharField(_('Css class'), null=True, blank=True,
        choices=consts.SLIDE_CSS_CLASSES, max_length=50)

    objects = SliderPhotoManager()

    class Meta:
        verbose_name = _('Slider photo')
        verbose_name_plural = _('Slider photos')
        ordering = ('order',)

    def __unicode__(self):
        return self.get_title()

    def get_title(self):
        return self.title or self.get_from_content_object('title')

    def get_image(self):
        return self.image or self.get_from_content_object('image')

    def get_video(self):
        return self.video or self.get_from_content_object('video')

    def get_description(self):
        return self.description or self.get_from_content_object('description')

    def get_absolute_url(self):
        if self.links_to:
            return self.links_to
        if self.content_object:
            return self.content_object.get_absolute_url()
        return '#'

    def get_from_content_object(self, field):
        if self.content_type:
            mapping_key = '%s.%s' % self.content_type.natural_key()
            mapping = consts.SLIDE_FIELDS_MAPPING.get(mapping_key)
            if mapping:
                field = mapping[field]
            return getattr(self.content_object, field, None)
        else:
            return getattr(self, field)
