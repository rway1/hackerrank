import os
from os import listdir
import difflib
import importlib
import re

file_to_be_tested = "executable"


def main():
    cwd = os.getcwd()
    common_prefix = os.path.commonprefix([cwd, os.path.abspath(__file__)])
    relative_path = cwd.replace(common_prefix, "")
    import_string = relative_path.replace("/", ".") + "." + file_to_be_tested
    module = importlib.import_module(import_string)
    module.RunCodeOnFile()
    

def FindExecutable():
    for file in listdir(path=dir_path):
        print(file)
        if re.search(".py", file):
            return file


if __name__ == "__main__":
    main()