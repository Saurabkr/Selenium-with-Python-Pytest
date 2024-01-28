# command to run single file : py.test <fileName> -v -s
# cmd to run the particular set of function from different files : py.test -k <functionWord> -v -s
# fixture is used to pass pre-requists or data before test cases runs

import pytest

def test_firstTestFunc(setup):
    print("Welcome to demo 2")

# used for not getting failing error in console, but running this test case is important
@pytest.mark.xfail
def test_BankInfo():
    a = 2
    b = 4
    assert b+2 == 6, "correct"



