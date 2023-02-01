import pytest
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():
    print("start browser")
    global driver
    driver= webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    driver.quit()
    print("close browser")

def test1(setup):
    driver.get("http://google.com")
    print("test1 executed")
def test1(setup):
    driver.get("http://facebook.com")
    print("test1 executed")
def test2(setup):
    driver.get("http://gmail.com")
    print("test2 executed")
def test3(setup):
    print("test3 executed")
