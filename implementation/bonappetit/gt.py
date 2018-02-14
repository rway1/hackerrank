import executable
from os import listdir
import difflib
import re


def main():
    executable.main(FindExecutable())

def FindExecutable():
    for file in listdir(path='.'):
        if re.match(".py", file):
            return file


if __name__ == "__main__":
    main()