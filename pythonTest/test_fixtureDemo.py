import pytest

@pytest.mark.usefixtures("dataLoad")
class TestExample:
  def test_demoFixture(self, dataLoad):
     print("First Name:", dataLoad[0])
     
     print("Last Name:", dataLoad[1])