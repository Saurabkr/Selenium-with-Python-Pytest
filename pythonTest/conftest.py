import pytest

@pytest.fixture(scope="class")
def setup():
    print("i am fixture method annotation")
    yield
    print("i will be run at last after all test cases passes")


@pytest.fixture()
def dataLoad():
    return ['saurab', 'kumar']

@pytest.fixture(params=[("Dev", "kumar", "SDET"), ("suman","gupta", "developer"),"Bamboobox"])
def crossBrower(request):
    return request.param
