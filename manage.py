import sys
import os
import re
import subprocess

messages = dict(
    commands='Commands\n' + '-'*10 + '\n * starttest\n * runtest'
)

if len(sys.argv) > 1:
    try:
        command = sys.argv[1].strip()
        if command == 'starttest':
            if len(sys.argv) < 3:
                raise Exception('starttest command requires a test name as parameter')
            param = sys.argv[2].strip()
            path = f'scripts/{param}.py'
            file = open(path, 'a')
            file.close()
            print(f'Test {path} created')
        elif command == 'runtest':
            if len(sys.argv) < 3:
                raise Exception('runtest command requires the test name as parameter')
            param = sys.argv[2].strip()

            script_exists = False
            for file in os.listdir('scripts'):
                if re.match(f'test_[0-9][0-9]_{param}.py', file):
                    script_exists = True
                    print(f'Execute {file}\n{"-"*20}\n')
                    subprocess.call(['python', f'.\\scripts\\{file}'], shell=True)
                    break
            if not script_exists:
                raise Exception(f'Test {param} was not found')
        else:
            print('Invalid command\n')
            print(messages['commands'])
    except NameError as e:
        print('Import Error: script not found')
    except Exception as e:
        print(f'\nError\n{"-"*20}\n{e}')
else:
    print(messages['commands'])