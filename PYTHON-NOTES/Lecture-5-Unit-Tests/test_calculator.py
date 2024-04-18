from calculator import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("Test failed")
    else:
        print("Test passed")

    if square(3) != 9:
        print("Test failed")
    else:
        print("Test passed")

if __name__ == "__main__":
    main()