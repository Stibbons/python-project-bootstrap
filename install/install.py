#!/usr/bin/env python

# Beware:
#  - this script is executed using the system's python, so with not easy control on which
#    packages are available. Same, we cannot directly install new ones using pip.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

####################################################################################################
# Default settings

settings = {
    'requires_root': True,
}

####################################################################################################
# Imports

import os
import subprocess
import sys
# Do *not* use optparse or argparse here, we are not sure on which version of python we are!


####################################################################################################
# Utility functions
####################################################################################################

####################################################################################################
# Color terminal

class bcolors(object):
    HEADER = '\033[95m'
    OKBLUE = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BOOT = '\033[94m'

    ENDC = '\033[0m'

# Do *not* use color when:
#  - on windows
#  - not in a terminal except if we are in Travis CI
if sys.platform.startswith('win32') or (not os.environ.get("TRAVIS") and not sys.stdout.isatty()):
    bcolors.HEADER = ''
    bcolors.OKBLUE = ''
    bcolors.OKGREEN = ''
    bcolors.WARNING = ''
    bcolors.FAIL = ''
    bcolors.BOLD = ''
    bcolors.UNDERLINE = ''

    bcolors.ENDC = ''

####################################################################################################
# Log functions


def flush():
    sys.stdout.flush()
    sys.stderr.flush()


def printNewSection(char):
    print(bcolors.OKBLUE + char * 79)
    flush()


def printInfo(text):
    print(bcolors.OKBLUE + bcolors.OKBLUE + "[INFO    ] " + bcolors.ENDC + text)
    flush()


def printError(text):
    print(bcolors.FAIL + "[ERROR   ] " + bcolors.ENDC + text, file=sys.stderr)
    flush()


def printCmd(text):
    print(bcolors.OKGREEN + "[CMD     ] " + bcolors.ENDC + text)
    flush()


def printRootCmd(text):
    print(bcolors.OKGREEN + "[ROOT CMD] " + bcolors.ENDC + text)
    flush()


def printCmdBg(text):
    print(bcolors.OKGREEN + "[CMD (bg)] " + bcolors.ENDC + text)
    flush()


def printDetail(text):
    print(bcolors.HEADER + "[DETAIL  ] " + bcolors.ENDC + text)
    flush()


def run(cmd, cwd=None, shell=False):
    printCmd("{0}".format(" ".join(cmd)))
    subprocess.check_call(cmd, shell=shell, cwd=cwd)


def runAsRoot(cmd, cwd=None, shell=False):
    if os.geteuid() != 0:
        cmd = ['sudo'] + cmd
        printRootCmd("{0}".format(" ".join(cmd)))
    else:
        printCmd("(already root) {0}".format(" ".join(cmd)))
    subprocess.check_call(cmd, shell=shell, cwd=cwd)


####################################################################################################
# run external tools methods

def call(cmd, cwd=None, shell=False):
    printCmd("{0}".format(" ".join(cmd)))
    return subprocess.call(cmd, shell=shell, cwd=cwd)


def runBackground(cmd, cwd=None, shell=False):
    printCmdBg(" ".join(cmd))
    subprocess.Popen(cmd, cwd=cwd, shell=shell)


def runAsRootIfNeeded(cmd, cwd=None, shell=False):
    if settings['requires_root']:
        runAsRoot(cmd, cwd=cwd, shell=shell)
    else:
        run(cmd, cwd=cwd, shell=shell)


####################################################################################################
# print usage to the user

def usage():
    print("Usage: ./install/install.sh [-l|-d|-b|-h]")
    print("")
    print("Uninstall with './install/uninstall.py'")

####################################################################################################
# parse command line

action = "none"

if len(sys.argv) > 1:
    args = sys.argv[:]
    while args:
        executable = args.pop(0)
        cmd = args.pop(0)
        if cmd == "-h":
            usage()
            sys.exit(0)
        else:
            raise Exception("Invalid parameter: {!r}".format(cmd))
else:
    action = "default_install"

if sys.version_info < (2, 6):
    raise "must use python 2.7.x. Current version is: {}.".format(sys.version_info)


####################################################################################################
# execute actions


printNewSection("=")
printInfo("Installing ppb command line tool")
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
src_path = os.path.join(root_path, "src")
printDetail("Installation source: {0}".format(src_path))
runAsRootIfNeeded(["pip", "install", "-e", src_path])
printInfo("Installation complete")
printNewSection("=")
