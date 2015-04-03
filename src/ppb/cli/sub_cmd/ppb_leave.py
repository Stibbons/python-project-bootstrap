from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ppb.cli.sub_cmd._sub_command import SubCommand

__all__ = ['PpbLeave']


class PpbLeave(SubCommand):
    name = "leave"
    help = "remove PPB capability in your project"

    def addParser(self, parser):
        parser.add_argument("--blabla",
                            help=("Lorem ipsum Amet culpa mollit esse sit ut ut esse"),
                            required=False,
                            action="store_true",
                            dest="blabl")

    def execute(self):
        raise Exception("TODO: ppb info")
