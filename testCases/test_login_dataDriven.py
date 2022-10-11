from pageObjects.LoginPage import LoginPage
from time import sleep
from utilities.logger import LogGen        # import our logger we have created
from utilities.readProperty import ReadConfig
from utilities import XLUtil

class Test_001_Login:
    url = ReadConfig.getBaseURL()
    excel_file = ReadConfig.getXcel()

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

        self.rows = XLUtil.getRowCount(self.excel_file, 'Sheet1')

        result = []

        for r in range(2, self.rows+1):
            self.userID = XLUtil.readData(self.excel_file, "Sheet1", r, 1)
            self.password = XLUtil.readData(self.excel_file, "Sheet1", r, 2)
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
            try:
                actual_page_title = self.driver.title
            except:
                actual_page_title = ''
            # log
            self.generateLog.info("Actual page title is: %s", actual_page_title)

            expect_page_title = "Guru99 Bank Manager HomePage"
            # log
            self.generateLog.info("Expected page title is: %s", expect_page_title)
            if actual_page_title == expect_page_title:
                self.generateLog.info("Test Case Passed.")
                self.lp.click_logout()
                self.lp.accept_alert()
                result.append("passed")
            else:
                self.generateLog.error("Test Case Failed.")
                result.append("failed")
        if "failed" not in result:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

