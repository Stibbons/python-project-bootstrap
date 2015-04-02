from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import pip

from setuptools import setup

version = "0.0.1"

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = pip.req.parse_requirements(os.path.join(os.path.dirname(__file__),
                                                       "requirements.txt"),
                                          session=pip.download.PipSession())

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]


setup_args = {
    'name': "ppb",
    'version': version,
    'entry_points': {
        'console_scripts': [
            'ppb = ppb.cli:run',
        ],
        'install_requires': reqs,
    },
}

setup(**setup_args)
