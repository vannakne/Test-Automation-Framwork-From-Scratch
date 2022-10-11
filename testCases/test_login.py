from pageObjects.LoginPage import LoginPage
from time import sleep
from utilities.logger import LogGen        # import our logger we have created
from utilities.readProperty import ReadConfig


class Test_001_Login:
    url = ReadConfig.getBaseURL()
    userID = ReadConfig.getUserID()
    password = ReadConfig.getPassword()

    generateLog = LogGen.genlog()

    # test case 01
    def test_login_with_valid_credential(self, setup):
        # log
        self.generateLog.info("********* Stard test_login_with_valid_credential ... *********")
        self.driver = setup
        # log
        self.generateLog.info("Go to %s", self.url)
        self.driver.get(self.url)
        sleep(0.3)

        self.lp = LoginPage(self.driver)

        # log
        self.generateLog.info("enter userID")
        self.lp.enter_userID(self.userID)
        # log
        self.generateLog.info("enter Password")
        self.lp.enter_password(self.password)
        # log
        self.generateLog.info("click login button")
        self.lp.click_login_btn()

        self.generateLog.info("Getting page title")
        actual_page_title = self.driver.title
        # log
        self.generateLog.info("Actual page title is: %s", actual_page_title)

        expect_page_title = "Guru99 Bank Manager HomePage"
        # log
        self.generateLog.info("Expected page title is: %s", expect_page_title)
        if actual_page_title == expect_page_title:
            assert True
            # log
            self.generateLog.info("Test Case Passed.")
            self.driver.close()
        else:
            # before we failed our test we will take a screenshot as a reference
            self.driver.save_screenshot("../screenshots/login_with_valid_credential.png")
            self.driver.close()
            # log
            self.generateLog.error("Test Case Failed.")
            assert False


     # test case 02
    def test_login_with_invalid_credential(self, setup):
        self.generateLog.info("********* Stard test_login_with_invalid_credential ... *********")
        self.driver = setup
        self.generateLog.info("Go to %s", self.url)
        self.driver.get(self.url)
        sleep(0.3)

        self.lp = LoginPage(self.driver)

        self.generateLog.info("enter valid userID")
        self.lp.enter_userID(self.userID)
        self.generateLog.info("enter invalid password")
        self.lp.enter_password("invalidPassword")
        self.generateLog.info("click login button")
        self.lp.click_login_btn()

        alert_message = self.lp.get_alert_message()
        self.generateLog.info("Actual alert message is: %s", alert_message)
        self.generateLog.info("accepted alert message")
        self.lp.dismiss_alert()

        expected_alert_message = "User or Password is not valid"
        self.generateLog.info("Expected alert message is: %s", expected_alert_message)
        if alert_message == expected_alert_message:
            assert True
            self.generateLog.info("Test Case Passed.")
            self.driver.close()
        else:
            self.driver.save_screenshot("../screenshots/test_login_with_invalid_credential.png")
            self.generateLog.info("Test Case Failed.")
            self.driver.close()
            assert False