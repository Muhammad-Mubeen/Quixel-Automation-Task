from appium import webdriver

class Test_002_Mobile:
    # cap = {
    #     "appium:deviceName": "Android Emulator",
    #     "platformName": "Android",
    #     "appium:udid": "emulator-5554",
    #     "appium:app": "D:\\Automation\\EZWeb.apk",
    #     "appium:automationName": "UiAutomator2"
    # }

    # kobitonServerUrl = 'https://talhaakhter:ca379d0e-df4d-4f77-8f5d-013e594975ad@api.kobiton.com/wd/hub'

    # desired_caps = {
    #     'sessionName': 'Automation test session',
    #     'sessionDescription': 'This is Automation Testing by Talha for Galaxy Note 10',
    #     'deviceOrientation': 'portrait',
    #     'captureScreenshots': False,
    #     # The maximum size of application is 1000MB
    #     # By default, HTTP requests from testing library are expired
    #     # in 2 minutes while the app copying and installation may
    #     # take up-to 30 minutes. Therefore, you need to extend the HTTP
    #     # request timeout duration in your testing library so that
    #     # it doesn't interrupt while the device is being initialized.
    #     'app': 'kobiton-store:423697',
    #
    #     # The given team is used for finding devices and the created session will be visible for all members within the team.
    #     'groupId': 3530,  # Group: AT Tech QA
    #     'deviceGroup': 'KOBITON',
    #     # For deviceName, platformVersion Kobiton supports wildcard
    #     # character *, with 3 formats: *text, text* and *text*
    #     # If there is no *, Kobiton will match the exact text provided
    #     'deviceName': 'Galaxy Note10+',
    #     'platformName': 'Android',
    #     'platformVersion': '12'
    # }

    kobitonServerUrl = 'https://talhaakhter:ca379d0e-df4d-4f77-8f5d-013e594975ad@api.kobiton.com/wd/hub'

    desired_caps = {
        'sessionName': 'Automation test session',
        'sessionDescription': 'This is Test Automation by Talha Akhter',
        'deviceOrientation': 'portrait',
        'captureScreenshots': True,
        # The maximum size of application is 1000MB
        # By default, HTTP requests from testing library are expired
        # in 2 minutes while the app copying and installation may
        # take up-to 30 minutes. Therefore, you need to extend the HTTP
        # request timeout duration in your testing library so that
        # it doesn't interrupt while the device is being initialized.
        'app': 'kobiton-store:423697',

        # The given team is used for finding devices and the created session will be visible for all members within the team.
        'groupId': 3530,  # Group: AT Tech QA
        'deviceGroup': 'KOBITON',
        # For deviceName, platformVersion Kobiton supports wildcard
        # character *, with 3 formats: *text, text* and *text*
        # If there is no *, Kobiton will match the exact text provided
        'deviceName': 'Galaxy A50',
        'platformName': 'Android',
        'platformVersion': '11'
    }
    def test_login_01(self):
        # self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities=self.cap)
        self.driver = webdriver.Remote('https://talhaakhter:ca379d0e-df4d-4f77-8f5d-013e594975ad@api.kobiton.com/wd/hub',
                                       desired_capabilities=self.desired_caps)
        # .driver = webdriver.Remote("http://localhost:4723/wd/hub", desself.cap)
        # Login scenario
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id('com.attech.attech_android_1.driq:id/btn_get_started').click()

        self.driver.find_element_by_id('com.attech.attech_android_1.driq:id/btn_sign_in').click()
        self.driver.find_element_by_id('com.attech.attech_android_1.driq:id/email').send_keys('aimantest@yopmail.com')
        self.driver.find_element_by_id('com.attech.attech_android_1.driq:id/password').send_keys('@Aiman@123')
        self.driver.find_element_by_id('com.attech.attech_android_1.driq:id/done_signin').click()
        self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()
        self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()
        self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_button').click()
        # self.driver.find_element_by_id('com.attech.attech_android_1.driq:id/tv_skip').click()

        # self.driver.implicitly_wait(30)