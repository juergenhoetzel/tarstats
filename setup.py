#! /usr/bin/env python3

from setuptools import setup

setup(
    name="tarstats",
    version=1.2,
    py_modules = [ "tarstats"],
    entry_points = '''
      [console_scripts]
      tarstats=tarstats:main
    ''',
)
