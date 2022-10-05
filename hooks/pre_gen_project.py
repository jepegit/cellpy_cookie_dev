import os
import re
import sys


MIN_CELLPY_VERSION = (0, 5)
cellpy_version = '{{ cookiecutter.cellpy_version }}'
_cellpy_version = cellpy_version.split(".")

too_old = False

if int(_cellpy_version[0]) < MIN_CELLPY_VERSION[0]:
    too_old = True
elif int(_cellpy_version[1]) < MIN_CELLPY_VERSION[1]:
    too_old = True

if too_old:
    print()
    print("OH NO!!!!")
    print(f"Your version of cellpy is too old - aborting!")
    sys.exit(1)

print(f"setting up project in the following directory: {os.getcwd()}")
