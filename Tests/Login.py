import os.path
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Login_class:
    driver = webdriver.Chrome()
    driver.maximize_window()
    def __init__(self, name, password):
        self.username = name
        self.pwd = password


    def Login_fuction(self):
        #driver = webdriver.Chrome()
        self.driver.get("https://staging-infinity.cosmicnode.com/login")
        time.sleep(2)
        page_heading = self.driver.find_element(By.XPATH, "//h3[text()='Account Login']").text
        assert "Account Login" in page_heading
        # Entering the Email id and password
        self.driver.find_element(By.NAME, "email").send_keys(self.username)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder ='Password']").send_keys(self.pwd)
        self.driver.find_element(By.CSS_SELECTOR, ".form-check-label").click()
        time.sleep(2)

        # Clicking on Login button
        self.driver.find_element(By.CLASS_NAME, "mt-3").click()
        time.sleep(5)
        #role_name = self.driver.find_element(By.XPATH, "//b[text()='Platform Owner']").text
        #assert "Platform Owner" in role_name

if __name__ == "__main__":
    login_obj = Login_class(name="platform-owner@cosmicnode.com", password="dUOktEGlWaWj_EIzumoiH#")
    login_obj.Login_fuction()
