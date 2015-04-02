from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class SubCommand(object):
    name = NotImplementedError
    help = NotImplementedError

    def addParser(self, parser):
        raise NotImplementedError

    def execute(self):
        raise NotImplementedError
