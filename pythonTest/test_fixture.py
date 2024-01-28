import pytest

# fixture is used same as @BeforeTest or @AfterTest in java. Fixture run starting of any test cases like pre-requisits
# i.e setting us env. or connecting db
# yield : use to execute at last ex: closing browser at end, disconnecting db or deleting cookies
# we can also write fixture in conftest file and use it throughout the test cases


# @pytest.fixture()
# def setup():
#     print("i am fixture method annotation")
#     yield
#     print("i will be run at last after all test cases passes")


# def test_afterFixture():
#     print("I will run after fixture")

# For example we have many testcases(function) which have fixture then we can define class of it and keep all
#function or test cases into it

@pytest.mark.usefixtures("setup")
class testCases:
    def test_fixturedemo(self):
        print("i am TC1")


    def test_fixturedemo1(self):
        print("i am TC2")

