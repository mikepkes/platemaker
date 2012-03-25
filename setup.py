from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='platemaker',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Michael Kessler',
      author_email='',
      url='',
      license='',
      packages=find_packages('src', exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          # I would like to require EITHER pyside or pyqt, but
          # Not sure what everybody prefers.
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      scripts = ['scripts/platemaker',],
      )
