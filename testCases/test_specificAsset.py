# import condition
import pytest
from selenium import webdriver
from appium import webdriver
from pageObjects.QuixlObjects.specificAssetPage import SpecficAsset
# from pageObjects.Dr_iQ.SelectImagePage import UploadPhotoFromGallery
# from utilities.readConfig import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.QuixlObjects.LoginPage import Login
from selenium.webdriver.common.keys import Keys
from appium.webdriver.mobilecommand import MobileCommand
import time
import allure
from allure_commons.types import AttachmentType

from utilities.readConfig import ReadConfig
import os.path
import time

class Test_specificAsset:
    # baseURL = "https://qa-app.dr-iq.com/login"
    # email = "ma@yopmail.com"
    # password = "Just4test@"

    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    # self.driver = setup
    # self.lp = Message(self.driver)



    def test_specificAsset(self , setup):


        # web

        self.logger.info("******Test_001_Download Asset******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()


        self.lp = SpecficAsset(self.driver)
        # self.lp.clickContentLicenseAgreementp()
        # self.lp.clickSkip()
        # self.lp.clickSignIn()
        # self.lp.clickSigninEpic()
        # time.sleep(2)
        # self.lp.clickEpicSignin()
        # self.driver.implicitly_wait(10)
        # self.lp.textEmail()
        # self.lp.textPassword()
        # self.lp.clickLogin()
        # time.sleep(15)

        self.lp.clickColor()
        self.lp.clickGray()
        time.sleep(2)
        self.lp.textSearch()
        # self.lp.clickStreet()
        # self.lp.clickManholeCover()
        # self.lp.textSearch()
        time.sleep(2)
        self.lp.hoverHugeIcelandicLav()
        self.lp.clickHugeIcelandicLav()
        self.lp.clickDownloadAsset()
        # self.lp.clickBeginForFree()
        # self.lp.clickContinueFreeTrial()
        # self.lp.clickGetStrated()
        # self.lp.clickContinueFreeTrial()
        # self.lp.clickResoulutionDropdown()
        # self.lp.click2kResolution()
        # self.lp.clickDownload2k()


