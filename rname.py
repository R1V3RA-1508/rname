#!/bin/python
# Usage: rname <old filename> <new filename>

import os
import sys
from argparse import ArgumentParser

parser = ArgumentParser(prog="rname", description="rename but better")
parser.add_argument("oldname", help="Old filename", type=str)
parser.add_argument("newname", help="New filename", type=str)
args = parser.parse_args()

if args.oldname == args.newname:
    print(
        f"No, you don't need to rename {args.oldname} to {args.newname}. The file's name is same"
    )
    sys.exit(0)
try:
    os.rename(args.oldname, args.newname)
    print(f"Successfully renamed {args.oldname} to {args.newname}")
    sys.exit(0)
except FileNotFoundError:
    print(f"ERROR: {args.oldname} not exists")
    sys.exit(1)
except PermissionError:
    print("ERROR: Not enough permissions")
    sys.exit(1)
except Exception:
    print("ERROR: Unknown error")
    sys.exit(1)
