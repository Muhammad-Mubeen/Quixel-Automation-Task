from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DownloadAsset:
    button_signin_xpath = '/html/body/div[1]/div/div[1]/div/div[4]/div[1]/div[2]/div/span/button'
    button_signinEpic_xpath = '/html/body/div[1]/div/div[1]/div/div/form/div/div[1]/button'
    button_epicSignin_xpath = '//*[@id="login-with-epic"]/span'
    text_email_xpath = '//*[@id="email"]'
    text_password_xpath = '//*[@id="password"]'
    button_login_xpath = '/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[5]/button/span/span'
    checkbox_contentLicenseAgreement_xpath = '/html/body/div[1]/div/div/div[2]/section/div[1]/div/label/div/label/span[1]/span'
    button_continue_xpath = '/html/body/div[1]/div/div/div[2]/section/div[2]/div/button'
    button_types_xpath = '/html/body/div[1]/div/div/div/div[4]/div[2]/div[1]/div/button/div/span'
    button_decals_xpath = '/html/body/div[1]/div/div/div/div[4]/div[2]/div[1]/div/div/ul/li[5]/button/span'
    button_street_xpath = '/html/body/div[1]/div/div/div/div[2]/div/div/section[1]/div/a[13]/span/div/div/div/div[2]/div/div/div[1]/div/h1'
    button_manholeCover_xpath = '/html/body/div[1]/div/div[1]/div/div[2]/div/div/section[1]/div/a[1]/span/div/div/div/div[2]/div'
    text_search_xpath = '//*[@id="app-page"]/div/div[4]/div[1]/div[1]/div/div/div/div[2]/div/input'
    button_roundDrainHole_xpath = '/html/body/div[1]/div/div/div/div[2]/div/div/section[2]/div/div/li[2]/div/a/span/div/div/div/div'
    button_downloadAsset_xpath = '/html/body/div[1]/div/div/div/div[2]/div/div/section[1]/div/div/li[2]/div/a/span/div/div/div/div/div[2]/svg'
    button_signInDownload_xpath = '//*[@id="app-page"]/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]/div/button'
    button_beginForFree_xpath = '/html/body/div[1]/div/div[1]/div/div[1]/section/div[2]/div[1]/span/span/a'
    button_continueFreeTrial_xpath = '/html/body/div[1]/div/div[2]/div/div/div[1]/div/div/div/div/section/div/section/div/section/div/div[2]/div/button'
    button_getStrated_xpath = '/html/body/div[1]/div/div[2]/div/div/div[1]/div/div/div/div/section/section/div[2]/div/a'
    button_resoulutionDropdown_xpath = '/html/body/div[1]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/span/svg'
    button_2kResolution_xpath = '/html/body/div[1]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/ul/li[1]/button'
    button_download2k_xpath = '/html/body/div[1]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]/div/button'

    def __init__(self, driver):
        self.driver = driver

    def clickContentLicenseAgreementp(self):
        self.driver.find_element_by_xpath(self.checkbox_contentLicenseAgreement_xpath).click()

    def clickSignIn(self):
        self.driver.find_element_by_xpath(self.button_signin_xpath).click()

    def clickSigninEpic(self):
        self.driver.find_element_by_xpath(self.button_signinEpic_xpath).click()

    def clickEpicSignin(self):
        self.driver.find_element_by_xpath(self.button_epicSignin_xpath).click()

    def textEmail(self):
        self.driver.find_element_by_xpath(self.text_email_xpath).send_keys("sdf")

    def textPassword(self):
        self.driver.find_element_by_xpath(self.text_password_xpath).send_keys('sdfds')

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickSkip(self):
        self.driver.find_element_by_xpath(self.button_continue_xpath).click()

    def clickType(self):
        self.driver.find_element_by_xpath(self.button_types_xpath).click()

    def clickDecals(self):
        self.driver.find_element_by_xpath(self.button_decals_xpath).click()

    def clickStreet(self):
        self.driver.find_element_by_xpath(self.button_street_xpath).click()

    def clickManholeCover(self):
        self.driver.find_element_by_xpath(self.button_manholeCover_xpath).click()

    def textSearch(self):
        self.driver.find_element_by_xpath(self.text_search_xpath).send_keys('round drain cover' + Keys.ENTER)

    def hoverRoundDrainHole(self):
        # hover = self.driver.find_element_by_xpath(self.button_roundDrainHole_xpath)
        # hover = ActionChains.move_to_element(self.driver,hover)
        # hover.perform()
        b = ActionChains(self.driver)
        hover2 = self.driver.find_element_by_xpath(self.button_roundDrainHole_xpath)
        b.move_to_element(hover2).perform()

    def clickRoundDrainHole(self):
        self.driver.find_element_by_xpath(self.button_roundDrainHole_xpath).click()

    def clickDownloadAsset(self):
        # Comment because no download button is appearing on automated chrome
        # self.driver.find_element_by_xpath(self.button_downloadAsset_xpath).click()
        self.driver.find_element_by_xpath(self.button_signInDownload_xpath).click()
    def clickBeginForFree(self):
        self.driver.find_element_by_xpath(self.button_beginForFree_xpath).click()

    def clickContinueFreeTrial(self):
        self.driver.find_element_by_xpath(self.button_continueFreeTrial_xpath).click()

    def clickGetStrated(self):
        self.driver.find_element_by_xpath(self.button_getStrated_xpath).click()

    def clickContinueFreeTrial(self):
        self.driver.find_element_by_xpath(self.button_continueFreeTrial_xpathh).click()

    def clickResoulutionDropdown(self):
        self.driver.find_element_by_xpath(self.button_resoulutionDropdown_xpath).click()

    def click2kResolution(self):
        self.driver.find_element_by_xpath(self.button_2kResolution_xpath).click()

    def clickDownload2k(self):
        self.driver.find_element_by_xpath(self.button_download2k_xpath).click()
