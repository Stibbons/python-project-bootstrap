from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from distutils.core import setup

version = "0.0.1"

setup_args = {
    'name': "ppb",
    'version': version,
    'entry_points': {
        'console_scripts': [
            'ppb = ppb.cli:run',
        ],
    },
}

setup(**setup_args)
