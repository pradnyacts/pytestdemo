import pytest
import sys
@pytest.mark.skip     #to skip the test
def test_login():
    print("login done")
@pytest.mark.skipif(sys.version_info<(3,10), reason="python version not supported")   #skip based on condtion
def test_addProduct():
    print("add product")

@pytest.mark.xfail
def test_logout():
    print("logout")

def test_close():
    assert True
    print("close")