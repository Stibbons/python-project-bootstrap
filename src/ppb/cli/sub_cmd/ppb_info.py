from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ppb.cli.sub_cmd._sub_command import SubCommand

__all__ = ['PpbInfo']


class PpbInfo(SubCommand):
    name = "info"
    help = "help message"

    def addParser(self, parser):
        parser.add_argument("--blabla",
                            help=("Lorem ipsum Amet culpa mollit esse sit ut ut esse"),
                            required=False,
                            action="store_true",
                            dest="blabl")

    def execute(self):
        raise Exception("TODO: ppb info")
