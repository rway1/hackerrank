import os
from os import listdir
import difflib
import importlib
import re
import sys
import filecmp


cwd = os.getcwd()
test_directory_name = "tests"
result_directory_name = "results"
test_directory = cwd + "/" + test_directory_name
file_to_be_tested = "executable"
output_file_regex = "\w+.out"
output_file_ext = ".out"
input_file_regex = "\w+.in"
input_file_ext = ".in"
result_file_ext = ".myout"
command = ["python3", "", "<", "", ">", ""]


def main():
    executable = GetExecutable()
    test_dictionary = GetTestDictionary()
    i = 1
    for input_file, output_file in test_dictionary.items():
        result_file = input_file.replace(input_file_ext, result_file_ext).replace(test_directory_name, result_directory_name)
        command[1] = executable
        command[3] = input_file
        command[5] = result_file
        os.system(' '.join(command))
        if filecmp.cmp(output_file, result_file):
            print("test " + str(i) + " passed")
        else:
            print("test " + str(i) + " failed")
        i = i + 1

def GetTestDictionary():
    if not os.path.exists(test_directory):
        print("Test Directory Not Found")
        sys.exit()
        
    all_test_files = os.listdir(test_directory)
    test_in_files = [
        test_directory_name + "/" + file_name for file_name in all_test_files
            if re.match(input_file_regex, file_name)
    ]
    
    test_dictionary = dict.fromkeys(test_in_files)
    for input_file in test_in_files:
        output_file = input_file.replace(input_file_ext, output_file_ext)
        if os.path.exists(output_file):
            test_dictionary[input_file] = output_file
        else:
            print("No matching output file: " + output_file + " for: " + input_file)
            
    return test_dictionary


def GetExecutable():
    cwd = os.getcwd()
    return cwd + "/" + file_to_be_tested + ".py"



if __name__ == "__main__":
    main()