#!/usr/bin/env python
# Module:   main
# Date:     25th May 2015
# Author:   James Mills, prologic at shortcircuit dot net dot au


"""Tool for creating and managing Docker Machines"""

from __future__ import print_function

from os import environ
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser


from .api import Factory
from .version import version


def cmd_up(factory, args):
    factory.up(args.file, detached=args.detached)


def parse_args():
    parser = ArgumentParser(
        description=__doc__,
        version=version,
        formatter_class=ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-f", "--file", dest="file", metavar="FILE", type=str,
        default=environ.get("FACTORY_FILE", environ.get("FILE", "factory.yml")),
        help="Specify an alternate factory file"
    )

    parser.add_argument(
        "--verbose", dest="verbose",
        action="store_true", default=False,
        help="Show more output"
    )

    subparsers = parser.add_subparsers(
        title="Commands", metavar="[Command]",
    )

    # up
    up_parser = subparsers.add_parser(
        "up",
        help="Bring up all machines"
    )
    up_parser.set_defaults(func=cmd_up)

    up_parser.add_argument(
        "-d", dest="daemon",
        action="store_true", default=False,
        help="Detached mode; Bring up machines in the background"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    factory = Factory()

    args.func(factory, args)


if __name__ == "__main__":
    main()
