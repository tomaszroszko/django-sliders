from django.contrib import admin
from sliders.models import SliderPhoto, Slider


class SliderPhotoAdmin(admin.TabularInline):
    model = SliderPhoto
    sortable_field_name = "order"
    extra = 0

class SliderAdmin(admin.ModelAdmin):

    inlines = (SliderPhotoAdmin,)


admin.site.register(Slider, SliderAdmin)