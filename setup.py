import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-sliders',
    version='0.3.4',
    packages=['sliders', 'sliders.migrations', 'sliders.templatetags'],
    include_package_data=True,
    license='BSD License',
    description='django application to store and display photo sliders in your page',
    long_description=README,
    url='https://github.com/tomaszroszko/django-sliders',
    author='Tomasz Roszko',
    author_email='tomaszroszko@gmail.com',
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
)