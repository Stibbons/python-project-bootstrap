#!/usr/bin/env python

# Beware:
#  - this script is executed using the system's python, so with not easy control on which
#    packages are available. Same, we cannot directly install new ones using pip.
#  - the role of the first stage of this installer is just to install a fresh new virtualenv
#    with a *controled* version of python, pip and virtualenv, and launch the second part of
#    the installer, 'install-stage2.py', which will run in the virtualenv.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


settings = {
    'requires_root': True,
}

import os
import subprocess
import sys

# Do *not* use optparse or argparse here, we are not sure on which version of python we are!

do_virtualenv = True


def printNewSection(char):
    print(char * 79)


def printInfo(text):
    print("[INFO    ] " + text)


def printError(text):
    print("[ERROR   ] " + text)


def printCmd(text):
    print("[CMD     ] " + text)


def printRootCmd(text):
    print("[ROOT CMD] " + text)


def printCmdBg(text):
    print("[CMD (bg)] " + text)


def printDetail(text):
    print("[DETAIL  ] " + text)


def run(cmd, cwd=None, shell=False):
    printCmd("{0}".format(" ".join(cmd)))
    subprocess.check_call(cmd, shell=shell, cwd=cwd)


def runAsRoot(cmd, cwd=None, shell=False):
    cmd = ['sudo'] + cmd
    printRootCmd("{0}".format(" ".join(cmd)))
    subprocess.check_call(cmd, shell=shell, cwd=cwd)


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


def usage():
    print("Usage: ./install/install.sh [-l|-d|-b|-h]")
    print("")
    print("Uninstall with './install/uninstall.py'")

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


printNewSection("=")
printInfo("Installing ppb command line tool")
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
src_path = os.path.join(root_path, "src")
printDetail("Installation source: {0}".format(src_path))
runAsRootIfNeeded(["pip", "install", "-e", src_path])
printInfo("Installation complete")
printNewSection("=")
