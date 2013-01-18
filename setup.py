#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
clihub
------

clihub is a tool to interact with the APIv3 of GitHUB.

"""
from setuptools import setup
from setuptools import find_packages
from clihub import release


setup(
    name=release.name,
    version=release.version,
    url='http://github.com/matrixise/clihub',
    author='Stephane Wirtel',
    author_email='stephane@wirtel.be',
    install_requires=[
        'docopt',
        'requests',
    ],
    packages=find_packages(),
    platforms='any',
    zip_safe=False,
    entry_points="""
    [console_scripts]
    clihub = clihub.scripts.clihub:main
    """
)
