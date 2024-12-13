import main  # The code to test

def test_one():
    assert main.mirrorMe([1, 2, 3, 8, 9, 3, 2, 1]) == 3

def test_two():
    assert main.mirrorMe([6,7,8,9,1,2,9,8,7,6]) == 4

def test_three():
    assert main.mirrorMe([5,6,7,1,2,3,7,6,5]) == 3

def test_four():
    assert main.mirrorMe([8,1,2,3,4,5,6,7,8]) == 1
