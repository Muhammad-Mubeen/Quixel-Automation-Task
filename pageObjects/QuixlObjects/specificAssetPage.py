from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SpecficAsset:
    button_signin_xpath = '/html/body/div[1]/div/div[1]/div/div[4]/div[1]/div[2]/div/span/button'
    button_signinEpic_xpath = '/html/body/div[1]/div/div[1]/div/div/form/div/div[1]/button'
    button_epicSignin_xpath = '//*[@id="login-with-epic"]/span'
    text_email_xpath = '//*[@id="email"]'
    text_password_xpath = '//*[@id="password"]'
    button_login_xpath = '/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[5]/button/span/span'
    checkbox_contentLicenseAgreement_xpath = '/html/body/div[1]/div/div/div[2]/section/div[1]/div/label/div/label/span[1]/span'
    button_continue_xpath = '/html/body/div[1]/div/div/div[2]/section/div[2]/div/button'
    button_color_xpath = '//*[@id="app-page"]/div/div[4]/div[2]/div[5]/div/button/div/span'
    button_decals_xpath = '/html/body/div[1]/div/div/div/div[4]/div[2]/div[5]/div/div/ul/li[5]/button/span'
    button_gray_xpath = '//*[@id="app-page"]/div/div[4]/div[2]/div[5]/div/div/ul/li[5]/button/span'
    button_manholeCover_xpath = '/html/body/div[1]/div/div[1]/div/div[2]/div/div/section[1]/div/a[1]/span/div/div/div/div[2]/div'
    text_search_xpath = '//*[@id="app-page"]/div/div[4]/div[1]/div[1]/div/div/div/div[2]/div/input'
    button_hugeIcelandicLava_xpath = '//*[@id="content-scroll-container"]/div/section[2]/div/div/li/div/a/span/div/div/div/div'
    button_downloadAsset_xpath = '/html/body/div[1]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]/div/button'
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

    def clickColor(self):
        self.driver.find_element_by_xpath(self.button_color_xpath).click()

    def clickGray(self):
        self.driver.find_element_by_xpath(self.button_gray_xpath).click()

    def clickStreet(self):
        self.driver.find_element_by_xpath(self.button_street_xpath).click()

    def clickManholeCover(self):
        self.driver.find_element_by_xpath(self.button_manholeCover_xpath).click()

    def textSearch(self):
        self.driver.find_element_by_xpath(self.text_search_xpath).send_keys('siEoZ' + Keys.ENTER)

    def hoverHugeIcelandicLav(self):
        # hover1 = self.driver.find_element_by_xpath(self.button_hugeIcelandicLava_xpath)
        # hover = ActionChains.move_to_element(self.driver,hover1)
        # hover.perform()
        a = ActionChains(self.driver)
        hover1 = self.driver.find_element_by_xpath(self.button_hugeIcelandicLava_xpath)
        a.move_to_element(hover1).perform()


    def clickHugeIcelandicLav(self):
        self.driver.find_element_by_xpath(self.button_hugeIcelandicLava_xpath).click()

    def clickDownloadAsset(self):
        self.driver.find_element_by_xpath(self.button_downloadAsset_xpath).click()

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
