import sys
import os
import re
import importlib
import functools
import unittest

class ManageException(BaseException):
     def __init__(self, message) -> None:
          super().__init__(message)

modules = ['selenium_introduction', 'unittest_examples', 'pytest_examples', 'practice']

messages = dict(
    commad_format='python manage.py module_name script_name',
    modules=functools.reduce(lambda a, b: f'{a}, {b}', modules)
)

try:
    if len(sys.argv) < 3:
        raise ManageException(f'FORMAT ERROR: correct format is "{messages["commad_format"]}"')
    module = sys.argv[1]
    if module not in modules:
        raise ManageException(f'MODULE ERROR: available modules are {messages["modules"]}')
    script = sys.argv[2]
    script_exists = False
    for file in os.listdir(module):
        if re.match(f'test_[0-9][0-9]_{script}.py', file):
            print(f'Execute {file}\n{"-"*20}\n')
            script_exists = True
            m = importlib.import_module(f'{module}.{file[:-3]}')
            if m.__getattribute__('unittest') != None:
                 suite = unittest.TestLoader().loadTestsFromModule(m)
                 unittest.TextTestRunner().run(suite)
            break
    if not script_exists:
        raise ManageException(f'script {script} in module {module} was not found')
except ManageException as e:
        print(e.args)
