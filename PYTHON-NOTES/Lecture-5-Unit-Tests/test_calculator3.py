from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16

def test_square2():
    assert square(-3) == 9
    assert square(-2) == 4
    assert square(0) == 0


# Run the tests
# pytest test_calculator3.py

