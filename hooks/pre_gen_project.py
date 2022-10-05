import os
import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
cellpy_version = '{{ cookiecutter.cellpy_version }}'

# print(module_name)
print(cellpy_version)
#
# if not re.match(MODULE_REGEX, module_name):
#     print('ERROR: %s is not a valid Python module name!' % module_name)
#
#     # exits with status 1 to indicate failure
#     sys.exit(1)

print(f"setting up project in the following directory: {os.getcwd()}")
