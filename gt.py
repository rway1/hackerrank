import os
from os import listdir
import difflib
import importlib
import re
import sys

file_to_be_tested = "executable"
test_directory_name = "tests"
output_file_regex = "\w+.out"
output_file_ext = ".out"
input_file_regex = "\w+.in"
input_file_ext = ".in"


def main():
    module = GetModule()
    test_dictionary = GetTestDictionary()
    print(test_dictionary)



def GetTestDictionary():
    cwd = os.getcwd()
    test_directory = cwd + "/" + test_directory_name
    if not os.path.exists(test_directory):
        print("Test Directory Not Found")
        sys.exit()
        
    all_test_files = os.listdir(test_directory)
    test_in_files = [
        file_name for file_name in all_test_files
            if re.match(input_file_regex, file_name)
    ]
    
    test_dictionary = dict.fromkeys(test_in_files)
    for input_file in test_in_files:
        output_file = input_file.replace(input_file_ext, output_file_ext)
        if not os.path.exists(test_directory + "/" + output_file):
            print("No matching output file: " + output_file + " for: " + input_file)
        else:
            test_dictionary[input_file] = output_file
    return test_dictionary


def GetModule():
    cwd = os.getcwd()
    common_prefix = os.path.commonprefix([cwd, os.path.abspath(__file__)])
    relative_path = cwd.replace(common_prefix, "")
    import_string = relative_path.replace("/", ".") + "." + file_to_be_tested
    try:
        return importlib.import_module(import_string)
    except:
        print("No Module Found: " + import_string)
        sys.exit()



if __name__ == "__main__":
    main()