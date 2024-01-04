import sys
import importlib

if len(sys.argv) > 1:
    try:
        lib = importlib.import_module(f'scripts.{sys.argv[1]}')
    except NameError as e:
        print('Import Error: script not found')
    except Exception as e:
        print(f'Error {e}')