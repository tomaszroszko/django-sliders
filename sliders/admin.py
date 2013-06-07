from django.contrib import admin
from sliders.models import SliderPhoto, Slider


class SliderPhotoAdmin(admin.TabularInline):
    model = SliderPhoto


class SliderAdmin(admin.ModelAdmin):

    inlines = (SliderPhotoAdmin,)


admin.site.register(Slider, SliderAdmin)