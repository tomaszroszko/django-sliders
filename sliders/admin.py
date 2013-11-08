from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from sliders.models import SliderPhoto, Slider


class SliderPhotoAdmin(admin.StackedInline):
    model = SliderPhoto
    sortable_field_name = "order"
    extra = 0
    fieldsets = (
        (_('Slide Content'), {
            'fields': ('image', 'title', 'description', 'links_to'),
            'classes': ("grp-collapse grp-close grp-closed",),
            'description': _('Fill those fields only if you do not connect'
            ' slide with any content')
        }),
        (_('Connect Content'), {
            'fields': ('content_type', 'object_id'),
            'classes': ("grp-collapse grp-close grp-closed",),
            'description': _('Connect with content (news, article...), you do'
            'not need to put slide content manualy then')
        }),
        (_('Activity'), {
            'fields': ('is_active', 'active_from', 'active_to'),
            'classes': ("grp-collapse grp-close grp-closed",)
        }),
        (None, {
            'fields': ('order','css_class')
        })
    )

    related_lookup_fields = {
        'generic': (('content_type', 'object_id'),),
    }

class SliderAdmin(admin.ModelAdmin):

    inlines = (SliderPhotoAdmin,)


admin.site.register(Slider, SliderAdmin)