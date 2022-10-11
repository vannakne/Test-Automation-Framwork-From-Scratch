# import selenium libray
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

# loginPage Class
class LoginPage:
    # userID field element locator
    textbox_userId_xpath = '/html/body/form/table/tbody/tr[1]/td[2]/input'

    # userID error message element locator
    msg_userID_xpath = '//*[@id="message23"]'

    # password field element locator
    textbox_password_xpath = '/html/body/form/table/tbody/tr[2]/td[2]/input'

    # password error message element locator
    msg_password_xpath = '//*[@id="message18"]'

    # login button element locator
    btn_login_xpath = '/html/body/form/table/tbody/tr[3]/td[2]/input[1]'

    # reset button element locator
    btn_reset_xpath = '/html/body/form/table/tbody/tr[3]/td[2]/input[2]'

    btn_logout_xpath = '/html/body/div[3]/div/ul/li[15]/a'

    ################### Constructor ###################
    def __init__(self, driver):
        self.driver = driver


    ################### Basic action on each element ###################

    # input userId in userID field
    def enter_userID(self, userID):
        self.driver.find_element(By.XPATH, self.textbox_userId_xpath).send_keys(userID)

    # get error message of userID
    def get_userID_error_message(self):
        actual_msg = self.driver.find_element(By.XPATH, self.msg_userID_xpath).text
        return actual_msg

    # input password in Password field
    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    # get error message of password
    def get_password_error_message(self):
        actual_msg = self.driver.find_element(By.XPATH, self.msg_password_xpath).text
        return actual_msg

    # click login button
    def click_login_btn(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    # click reset button
    def click_reset_btn(self):
        self.driver.find_element(By.XPATH, self.btn_reset_xpath).click()

    # get actual message from alert popup
    def get_alert_message(self):
        alert = Alert(self.driver)
        return alert.text

    # accept the popup alert
    def accept_alert(self):
        alert = Alert(self.driver)
        alert.accept()

    # dismiss the popup alert
    def dismiss_alert(self):
        alert = Alert(self.driver)
        alert.dismiss()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.btn_logout_xpath).click()