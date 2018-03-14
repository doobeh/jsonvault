# -*- coding: utf-8 -*-
"""
    JSONVault Setup
    ~~~~~~~~~~~~
    Let's setup the application.
    :copyright: (c) 2018 by Anthony Plunkett.
    :license: BSD, see LICENSE for more details.
"""

from setuptools import setup, find_packages

setup(
    name='jsonvault',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-gunicorn',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)