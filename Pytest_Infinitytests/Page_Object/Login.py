import os.path
import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Page_Object.Tenant import TenantPage

@pytest.mark.usefixtures("browserInstance")
class Login_page():
    def __init__(self, driver, name, pwd, url):
        self.driver = driver
        self.username = name
        self.pwd = pwd
        self.url = url
        self.username_input = (By.NAME, "email")
        self.pwd_input = (By.CSS_SELECTOR, "input[placeholder ='Password']")
        self.showpwd_checkbox = (By.CSS_SELECTOR, ".form-check-label")
        self.login_button = (By.CLASS_NAME, "mt-3")


    def Login(self):
        self.driver.get(self.url)
        time.sleep(2)
        page_heading = self.driver.find_element(By.XPATH, "//h3[text()='Account Login']").text
        assert "Account Login" in page_heading
        # Entering the Email id and password
        self.driver.find_element(*self.username_input).send_keys(self.username)
        self.driver.find_element(*self.pwd_input).send_keys(self.pwd)
        self.driver.find_element(*self.showpwd_checkbox).click()
        time.sleep(2)

        # Clicking on Login button
        self.driver.find_element(*self.login_button).click()
        time.sleep(5)
        tenantpage_obj = TenantPage(self.driver)
        return tenantpage_obj

        #role_name = self.driver.find_element(By.XPATH, "//b[text()='Platform Owner']").text
        #assert "Platform Owner" in role_name


