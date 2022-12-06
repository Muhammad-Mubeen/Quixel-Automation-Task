from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup():
    # s = Service("D:\\Automation\\chromedriver_win32\\chromedriver.exe")
    # driver = webdriver.Chrome(service=s)
    # driver = webdriver.Chrome("C:\\Ali\\chromedriver.exe")
    driver = webdriver.Chrome(executable_path="C:\Ali\chromedriver.exe")
    return driver

@pytest.fixture()
def setup1():
    desired_cap = {
        "deviceName": "Android Emulator",
        "platformName": "Android",
        "appPackage": "com.attech.attech_android_1.driq",
        "app": "C:\\Ali\\app-debug.apk",
        "newCommandTimeout": "300"}

    driver1 = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    return driver1
    driver1.implicitly_wait(50)
# Pytest HTML Reporting

# def pytest_configure(config):
#     config._metadata['Project Name'] = 'QA Automation Framework Reporting'
#     config._metadata['Module Name'] = 'Module Name Framework'
#     config._metadata['Tester'] = 'Talha Akhter'

# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)