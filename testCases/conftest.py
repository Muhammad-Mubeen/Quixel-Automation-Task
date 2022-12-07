from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup():
    # s = Service("D:\\Automation\\chromedriver_win32\\chromedriver.exe")
    # driver = webdriver.Chrome(service=s)
    driver = webdriver.Chrome("C:\\chromedriver.exe")
    return driver

# Pytest HTML Reporting

def pytest_configure(config):
    config._metadata['Project Name'] = 'QA Automation Framework Reporting'
    config._metadata['Module Name'] = 'Module Name Framework'
    config._metadata['Tester'] = 'M Mubeen'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)