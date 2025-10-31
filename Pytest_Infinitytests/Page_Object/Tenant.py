import os
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TenantPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.tenant_name = None


    def tenantCreate(self, tenant_name):
        self.tenant_name = tenant_name
        time.sleep(2)
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

    def tenantAdminCreate(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CSS_SELECTOR, ".user-btn").click()
        self.driver.find_element(By.XPATH, "//button[text()='tenant admin']").click()
        self.driver.find_element(By.NAME, "name").send_keys(self.tenant_name)
        self.mail_address = (self.tenant_name.replace(" ", "").lower()) + "4@mailinator.com"
        self.driver.find_element(By.NAME, "userEmail").send_keys(self.mail_address)
        self.driver.find_element(By.NAME, "userEmail").send_keys(Keys.TAB)
        time.sleep(3)

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

    def tenantDelete(self, tenant_name):
        self.driver.find_element(By.XPATH, f"//h4[text()='{tenant_name}']/following::div[@class='dropdown'][1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Delete')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Ok')]").click()
        time.sleep(5)

    def tenantLogout(self):
        self.driver.find_element(By.XPATH, "//li[@class='dashboard-btn']").click()
        time.sleep(2)
        logout_path = "(//button[contains(@class,'border-0')])[3]"
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, logout_path)))
        self.driver.find_element(By.XPATH, logout_path).click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Account Login']")))


