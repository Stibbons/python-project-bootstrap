from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import pip
import re

from setuptools import find_packages
from setuptools import setup

# inspiration:
# https://github.com/jmcarp/robobrowser/pull/32/files#diff-2eeaed663bd0d25b7e608891384b7298L9


def find_version(fname):
    """
    Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    """

    version = ''
    with open(fname, 'r') as fp:
        major = None
        minor = None
        patch = None
        custom = None
        re_major = re.compile(r'^major = ([0-9]+)')
        re_minor = re.compile(r'^minor = ([0-9]+)')
        re_patch = re.compile(r'^patch = ([0-9]+)')
        re_custom = re.compile(r'^custom = ([a-zA-Z0-9\-_]+)')
        for line in fp:
            m = re_major.match(line)
            if m:
                major = m.group(1)
            m = re_minor.match(line)
            if m:
                minor = m.group(1)
            m = re_patch.match(line)
            if m:
                patch = m.group(1)
            m = re_custom.match(line)
            if m:
                custom = m.group(1)
        if not custom or custom == "None":
            return "{0}.{1}.{2}".format(major, minor, patch)
        else:
            return "{0}.{1}.{2}{3}".format(major, minor, patch, custom)
    if not version:
        raise RuntimeError('Cannot find version information')
    return version

__version__ = find_version(os.path.join(os.path.dirname(__file__),
                                        "ppb",
                                        "cli",
                                        "version.py"))

print("Setuptool for ppb version {0}".format(__version__))

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = pip.req.parse_requirements(os.path.join(os.path.dirname(__file__),
                                                       "requirements.txt"),
                                          session=pip.download.PipSession())

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]


setup_args = {
    'name': "ppb",
    'version': __version__,
    'description': 'command line tool for Python Project Bootstrap',
    'author': 'Gaetan Semet',
    'author_email': 'gaetan@xeberon.net',
    'url': 'https://github.com/Stibbons/python-project-bootstrap',
    'packages': find_packages(),
    'package_dir': {
        'ppb': 'ppb'
    },
    'include_package_data': True,
    'install_requires': reqs,
    'license': 'MIT',
    'zip_safe': False,
    'keywords': 'python, bootstrap, project',
    'classifiers': [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    'test_suite': 'ppb',
    'entry_points': {
        'console_scripts': [
            'ppb = ppb.cli:run',
        ],
    },
}

setup(**setup_args)
