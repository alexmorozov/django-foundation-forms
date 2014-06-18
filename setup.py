# -*- coding:utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))


# Get the description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    description = f.read()


setup(
    name='django-foundation-forms',
    version='0.1',
    url='http://github.com/alexmorozov/django-foundation-forms',
    author='Alex Morozov',
    author_email='am@kupo.la',
    description=description,
    license='GPL',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[
        'Django>=1.5',
        'hamlpy',
    ],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
