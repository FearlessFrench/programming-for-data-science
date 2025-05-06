

def test_ones_digit():
    print("Testing ones_digit...", end='')
    assert ones_digit(123) == 3
    assert ones_digit(7890) == 0
    assert ones_digit(6) == 6
    assert ones_digit(54) == 4
    print("Passed all tests!")

def ones_digit(x):
    return abs(x) % 10
test_ones_digit()