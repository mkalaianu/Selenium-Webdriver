import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class MailinatorPage:
    def __init__(self, password, driver):
        self.password = password
        self.driver = driver  # use existing browser

    def userInvite(self, name):
        self.driver.switch_to.new_window('tab')
        self.driver.get("https://www.mailinator.com/")
        time.sleep(2)
        #self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.LINK_TEXT, "GET FREE TRIAL").click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".modal-title")))
        #wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".close"))).click()
        self.driver.find_element(By.XPATH, "(//div[@class='modal-title']/following::button[@type='button'])[1]").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "inbox_field").clear()
        self.driver.find_element(By.ID, "inbox_field").send_keys(name)
        self.driver.find_element(By.CLASS_NAME, "primary-btn").click()
        #time.sleep(5)
        self.driver.find_element(By.XPATH, "(//td[contains(text(), 'Accept Invitation Mail')])[1]").click()
        self.driver.switch_to.frame("html_msg_body")
        #print(self.driver.find_element(By.TAG_NAME, "h2").text)
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Accept Invitation')]").click()
        self.driver.close()
        opened_windows = self.driver.window_handles
        #print(len(opened_windows))
        time.sleep(2)
        self.driver.switch_to.window(opened_windows[1])

        #self.driver.close()

    def userSetCredentials(self):
        try:
            self.driver.implicitly_wait(5)
            assert "User Invitation" == self.driver.find_element(By.TAG_NAME, "h5").text
            self.driver.find_element(By.NAME, "password").send_keys(self.password)
            self.driver.find_element(By.NAME, "confirmPassword").send_keys(self.password)
            time.sleep(2)
            self.driver.find_element(By.ID, "submit").click()
            time.sleep(2)
            #WebDriverWait(self.driver, 15).until(ec.presence_of_element_located((By.XPATH, "//div[contains(text()='Updated Successfully!')]")))
            warning_msg = self.driver.find_element(By.XPATH, "(//div[@role='alert'])[1]").text
            #print(warning_msg)
            if warning_msg == "Updated Successfully!":
                self.driver.close()
                return self.password

            else:
                new_pwd = int(self.password) + 1
                self.driver.find_element(By.NAME, "password").clear()
                self.driver.find_element(By.NAME, "password").send_keys(str(new_pwd))
                self.driver.find_element(By.NAME, "confirmPassword").clear()
                self.driver.find_element(By.NAME, "confirmPassword").send_keys(str(new_pwd))
                time.sleep(2)
                self.driver.find_element(By.ID, "submit").click()
                wait = WebDriverWait(self.driver, 10)
                wait.until(ec.presence_of_element_located((By.XPATH, "//div[contains(text(),'Updated Successfully!')]")))
                self.driver.close()
                return new_pwd


        except Exception as e:
            print(e)
        #print(len(self.driver.window_handles))
        #current_tab = self.driver.current_window_handle
        #if main_tab and current_tab != main_tab:
        #   self.driver.close()
            # Switch back to main application tab
        finally:
            opened_windows = self.driver.window_handles
            self.driver.switch_to.window(opened_windows[0])





