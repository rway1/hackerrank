import os
from os import listdir
import difflib
import importlib
import re
import sys

file_to_be_tested = "executable"


def main():
    module = FindModule()
    module.RunCodeOnFile()

def FindModule():
    cwd = os.getcwd()
    common_prefix = os.path.commonprefix([cwd, os.path.abspath(__file__)])
    relative_path = cwd.replace(common_prefix, "")
    try:
        import_string = relative_path.replace("/", ".") + "." + file_to_be_tested
        return importlib.import_module(import_string)
    except:
        print("No Module Found")
        sys.exit()



if __name__ == "__main__":
    main()