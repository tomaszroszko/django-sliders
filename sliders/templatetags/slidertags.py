from django import template
from sliders.models import SliderPhoto, Slider

register = template.Library()

@register.assignment_tag()
def sliders(slider_slug, limit=None):
    """
        slider_slug - string for Slider.slug_name
        limit - if None all Photos will be returned. Put int to limit number
        of photos

        usage: {% sliders slider_slug 5 as slider_items %}
    """
    queryset = SliderPhoto.objects.activated().filter(
        slider__slug_name=slider_slug)
    if limit:
        queryset = queryset[:limit]
    return queryset
