#!/bin/python
# Usage: rname <old filename> <new filename>

import os
import sys
from argparse import ArgumentParser


class SameNameError(Exception):
    pass


parser = ArgumentParser(prog="rname", description="rename but better")
parser.add_argument("oldname", help="Old filename", type=str)
parser.add_argument("newname", help="New filename", type=str)
args = parser.parse_args()

if args.oldname == args.newname:
    raise SameNameError(
        f"No, you don't need to rename {args.oldname} to {args.newname}. The file's name is same"
    )
try:
    os.rename(args.oldname, args.newname)
    print(f"Successfully renamed {args.oldname} to {args.newname}")
    sys.exit(0)
except FileNotFoundError:
    print(f"{args.oldname} not exists")
    sys.exit(1)
except PermissionError:
    print(f"Not enough permissions")
    sys.exit(1)
except Exception:
    print(f"Unknown error")
    sys.exit(1)
