import sys

def ReturnAString():
    return "String"

def main(argv):
    Print(argv)

def Print(args):
    print(args)

if __name__ == "__main__":
    main(sys.argv)