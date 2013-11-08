from django.conf import settings

SLIDE_CONTENT_TYPES = getattr(settings, 'SLIDE_CONTENT_TYPES', {})
SLIDE_FIELDS_MAPPING = getattr(settings, 'SLIDE_FIELDS_MAPPING', {})

SLIDE_CSS_CLASSES = getattr(settings, 'SLIDE_CSS_CLASSES', None)