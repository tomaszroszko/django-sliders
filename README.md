django-sliders
==============

django-slider is a django application to store and display photo sliders in
your page


Installation
------------

``pip install -e git+https://github.com/tomaszroszko/django-sliders.git#egg=django_sliders.git``

*settings.py*

```

INSTALED_APPS = (
    ...
    'sliders',
    ...
)
```

*run commands*

```
python manage.py syncdb
python manage.py migrate
```

*usage in tempmlates*

```
{% load slidertags %}
{# "main-slider" it's a slider slug_name #}
{# "3" it's a number of photos that need to be returned #}
{% sliders "main-slider" 3 as slider_items %}

```

