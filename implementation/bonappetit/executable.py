
if __name__ == "__main__":
    main()

def ReturnAString():
    return "String"

def main(inputfile):
    if ReturnAString() == open(inputfile).read():
        print("test passed")
    else:
        print("test failed")
