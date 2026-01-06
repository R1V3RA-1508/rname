#!/bin/python
# Usage: rname <old filename> <new filename>

import os
import sys
import logging
from argparse import ArgumentParser

parser = ArgumentParser(prog="rname", description="rename but better")
parser.add_argument("oldname", help="Old filename", type=str)
parser.add_argument("newname", help="New filename", type=str)
args = parser.parse_args()


def main():
    if args.oldname == args.newname:
        logging.error(
            f"No, you don't need to rename {args.oldname} to {args.newname}. The file's name is same"
        )
        sys.exit(0)
    try:
        os.rename(args.oldname, args.newname)
        logging.info(f"Successfully renamed {args.oldname} to {args.newname}")
        sys.exit(0)
    except FileNotFoundError:
        logging.error(f"{args.oldname} not exists")
        sys.exit(1)
    except PermissionError:
        logging.error("Not enough permissions")
        sys.exit(1)
    except Exception as e:
        logging.error(f"{e}")
        sys.exit(1)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, stream=sys.stdout, format="%(levelname)s: %(message)s"
    )
    main()
