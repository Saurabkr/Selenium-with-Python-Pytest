# Any pytest file should start or end with test_ or _test respectively
# method should start with test
# Any method should be wrapped in this function
# command to run this test in cmd py.test -v -s where -v -> verbose, -s => console log in output
# every method is treated as test case

import pytest

# used when we want to skid particular test cases
@pytest.mark.skip
def test_firstProgram():
    print("Hello World")

# used to run only that test case which have smoke mark on it
@pytest.mark.smoke
def test_BankName():
    print("welcome to SBI")