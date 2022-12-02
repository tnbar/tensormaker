# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


__author__ = "tnbar"
__version__ = "0.0.1"

setup(
      name='tensormaker',
      version=__version__,
      description='tensormaker: a powerful tensorizing toolkit based on Pytorch',
      author=__author__,
      maintainer=__author__,
      url='https://github.com/tnbar/tensormaker',
      packages=find_packages(),
      py_modules=[],
      long_description="A powerful tensorizing toolkit based on Pytorch.",
      license="BSD 3-Clause License",
      platforms=["any"],
      install_requires = []
)
