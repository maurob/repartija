#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import os

setup(
    name='repartija',
    version='0.1.0',
    description=u'Modelo para repartir dividendos con precios diferentes pero unificados',
    long_description=open('README.md').read(),
    author = u'Mauro Marcelo Bruni',
    author_email = 'maumarbru@gmail.com',
    url='http://github.com/maurob/repartija',
    py_modules=['repartija'],
    license='MIT',
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Spanish',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
