from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='myhack',
      version=0.1,
      description="trying",
      long_description="trying",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='myhack',
      author='minus79',
      author_email='gergely06@gmail.com',
      url='https://github.com/minus79/xenon',
      download_url = 'https://github.com/minus79/xenon/tarball/0.1',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
