import pytest
import  sys
@pytest.mark.parametrize(("username,password"),
                         [("selenium","webdriver"),("python","pytest"),("prad","desh")])
def test_login(username,password):
    print(username)
    print(password)