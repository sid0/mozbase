# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import os
from setuptools import setup, find_packages

version = '0.2'

# take description from README
here = os.path.dirname(os.path.abspath(__file__))
try:
    description = file(os.path.join(here, 'README.md')).read()
except (OSError, IOError):
    description = ''

setup(name='mozdevice',
      version=version,
      description="Mozilla-authored device management",
      long_description=description,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Mozilla Automation and Testing Team',
      author_email='tools@lists.mozilla.com',
      url='http://github.com/mozilla/mozbase',
      license='MPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      sut = mozdevice.sutcli:cli
      """,
      )
