from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from ppb.cli import sub_cmd
from ppb.cli import version

import argparse
import sys


class Main(object):

    '''
    This command line tool ...
    '''

    def main(self):

        # Global command-line arguments
        parser = argparse.ArgumentParser(description=self.__doc__)
        parser.add_argument('--debug', action='store_true', default=False,
                            help='Enable debugging output + automatic pdb attach on exception')
        parser.add_argument('--quiet', action='store_true', default=False,
                            help='Suppress output')
        parser.add_argument('-v', '--verbose', action='store_true', default=False,
                            help='Enable additional output')
        parser.add_argument('-V', '--version', action='version', version=version.version)

        subparser = parser.add_subparsers(title='Subcommands', description='Subcommands')

        for command_name in sub_cmd.__all__:
            sub_command = getattr(sub_cmd, command_name)()
            p = subparser.add_parser(sub_command.name, help=sub_command.help)
            p.set_defaults(subcommand=sub_command,
                           subsubcommand=sub_command.execute)
            sub_command.addParser(p)

        opts = parser.parse_args(sys.argv[1:])

        cmd = opts.subcommand
        cmd.options = opts

        cmd.execute()
