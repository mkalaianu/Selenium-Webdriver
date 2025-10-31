import os
import time

from selenium import webdriver
from selenium.webdriver import Keys
#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Login import Login_class
from mailinator import Mailinator


class Tenant:
    # driver = Login_class.driver
    #main_tab = ""

    def __init__(self, name, driver=None):
        #super().__init__(name="platform-owner@cosmicnode.com", password="dUOktEGlWaWj_EIzumoiH#")
        #super().Login_fuction()
        self.tenant_name = str(name)
        print(type(self.tenant_name))
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()


    def tenant_create(self):
        # self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

        self.driver.find_element(By.CSS_SELECTOR, ".add-new-item-btn").click()
        #time.sleep(3)
        self.driver.find_element(By.NAME, "businessName").send_keys(self.tenant_name)
        self.driver.find_element(By.NAME, "description").send_keys("This is the test tenant")
        self.driver.find_element(By.NAME, "businessTheme").send_keys("This is the test theme")
        self.driver.find_element(By.NAME, "locationAddress").send_keys("Eindhoven")
        self.driver.find_element(By.NAME, "url").send_keys("www.abc.com")
        #time.sleep(2)
        file_path = os.path.abspath("..//files/tenant.png")
        self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(file_path)
        #time.sleep(2)

        self.driver.find_element(By.XPATH,
                                 "//label[text()='Location']/following::div[contains(@class, 'css-1hwfws3')][1]").click()
        time.sleep(2)
        location_input = self.driver.find_element(By.XPATH, "//label[text()='Location']/following::input[1]")
        location_input.send_keys("Ind")
        #time.sleep(3)
        countries = self.driver.find_elements(By.XPATH, "//div[contains(@class,'option')]")
        print(len(countries))
        for country in countries:
            if country.text == "India":
                country.click()
                #time.sleep(2)
                break
        # location_input.send_keys(Keys.ENTER)
        # time.sleep(5)
        list_template = ['Building', 'Horticulture', 'Outdoor']
        for list_item in list_template:
            self.driver.find_element(By.XPATH, "//div[contains(@class,'css-nwjfc')]").click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, f"//div[text()='{list_item}']").click()
            #time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[text()='Outdoor']/following::div[@class='css-xb97g8'][1]").click()
        #time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='logo']").send_keys(file_path)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        #return self.main_tab

    def tenantadmin_create(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, ".user-btn").click()
        self.driver.find_element(By.XPATH, "//button[text()='tenant admin']").click()
        self.driver.find_element(By.NAME, "name").send_keys(self.tenant_name)
        self.mail_address = (self.tenant_name.replace(" ", "").lower()) + "2@mailinator.com"
        self.driver.find_element(By.NAME, "userEmail").send_keys(self.mail_address)
        self.driver.find_element(By.NAME, "userEmail").send_keys(Keys.TAB)
        time.sleep(5)

        self.driver.find_element(By.XPATH, "//div/input[@class='tenants-list-select__input']").send_keys(self.tenant_name)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div/input[@class='tenants-list-select__input']").send_keys(Keys.TAB)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        #self.main_tab = self.driver.current_window_handle
        #global mail_address
        #self.address_tab.append(self.mail_address)
        #self.address_tab.append(self.main_tab)

        return self.mail_address

    def tenant_collaborators(self):
        opened_windows = self.driver.window_handles
        self.driver.switch_to.window(opened_windows[0])
        time.sleep(2)
        self.driver.implicitly_wait(5)
        #self.driver.switch_to.window(self.main_tab)
        self.driver.find_element(By.XPATH, "//li[@class='dashboard-btn']").click()
        self.driver.find_element(By.XPATH,
                                 f"//h4[text()='{self.tenant_name}']/following::div[@class='dropdown'][1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Collaborators')]").click()
        time.sleep(2)
        assert self.mail_address == self.driver.find_element(By.XPATH, "//div[@class ='email']").text
        assert "Active" == self.driver.find_element(By.XPATH, "//div[contains(@class,'active-item')]").text
        self.driver.find_element(By.XPATH, "//div[contains(@class,'modal-title')]/button[contains(@class,'btn-primary')]").click()
        time.sleep(2)

    def tenant_delete(self):
        self.driver.find_element(By.XPATH, f"//h4[text()='{self.tenant_name}']/following::div[@class='dropdown'][1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Delete')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Ok')]").click()
        time.sleep(5)

if __name__ == "__main__":
    login_obj = Login_class(name="platform-owner@cosmicnode.com", password="dUOktEGlWaWj_EIzumoiH#")
    login_obj.Login_fuction()
    tenant_obj = Tenant("Tenant BCA", driver=Login_class.driver)
    tenant_obj.tenant_create()
    user_mail = tenant_obj.tenantadmin_create()
    user_username = (user_mail.split("@"))[0]
    print(user_username, user_mail)
    mailinator_obj = Mailinator("12345", driver=tenant_obj.driver)
    mailinator_obj.user_invite(user_username)
    user_password = mailinator_obj.user_setcredentials()
    print(user_password)
    tenant_obj.tenant_collaborators()
    #tenant_obj.tenant_delete()








