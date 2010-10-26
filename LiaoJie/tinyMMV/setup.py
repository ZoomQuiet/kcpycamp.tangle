#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name = 'Tiny MMV',
    version = '0.1',
    packages = ['tinymmv'],
    package_data = { 'tinymmv': [ '*.txt'] },

    author = "Richard Liao",
    author_email = 'richard.liao.i@gmail.com',
    maintainer = 'Richard Liao',
    maintainer_email = "richard.liao.i@gmail.com",
    description = "Tiny MMV for test bitten.",
    license = "BSD",
    keywords = "bitten mmv",
    url = "http://trac.rdev.kingsoft.net/camp",
    test_suite = "tinymmv.tests.test_tinymmv",
)
