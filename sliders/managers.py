from django.db import models
from django.db.models import Q
from django.utils.timezone import now


class SliderManager(models.Manager):
    """
        Manager for Slider class
    """
    def activated(self):
        """
            return only activated sliders
        """
        return self.filter(is_active=True)


class SliderPhotoManager(models.Manager):
    """
        Manager for SliderPhoto class
    """

    def activated(self):
        current = now()
        return self.filter(slider__is_active=True and
            Q(is_active=True) and
            (Q(active_from__isnull=True) or Q(active_from__lte=current)) and
            (Q(active_to__isnull=True) or Q(active_to__gte=current))
            )
