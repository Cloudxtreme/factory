#!/usr/bin/env python


"""Tool for creating and managing Docker Machines"""


from __future__ import print_function

from os import environ
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser


from yaml import load
from pathlib import Path
from attrdict import AttrDict


from .api import Factory
from .version import version


def cmd_ls(factory, args):
    factory.ls()


def cmd_up(factory, args):
    factory.up(args.file, detached=args.detached)


def cmd_stop(factory, args):
    factory.stop(args.machines)


def cmd_rm(factory, args):
    factory.rm(args.machines)


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

    # ls
    ls_parser = subparsers.add_parser(
        "ls",
        help="List all machines"
    )
    ls_parser.set_defaults(func=cmd_ls)

    # up
    up_parser = subparsers.add_parser(
        "up",
        help="Bring up all machines"
    )
    up_parser.set_defaults(func=cmd_up)

    # stop
    stop_parser = subparsers.add_parser(
        "stop",
        help="Stop a machine or all machines"
    )
    stop_parser.set_defaults(func=cmd_stop)

    stop_parser.add_argument(
        "machines", nargs="*",
        help="Machine to stop (optional)"
    )

    # rm
    rm_parser = subparsers.add_parser(
        "rm",
        help="Remove a machine or all machines"
    )
    rm_parser.set_defaults(func=cmd_rm)

    rm_parser.add_argument(
        "machines", nargs="*",
        help="Machine to stop (optional)"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    config = AttrDict(load(Path(args.file).resolve().open("r")))
    factory = Factory(config)

    args.func(factory, args)


if __name__ == "__main__":
    main()
