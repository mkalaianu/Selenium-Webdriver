import ftplib
import os.path
import sys
import time

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from . import ReadFile

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
customer_data = ReadFile.read_file()

class CustomerPage():
    def __init__(self, tenant_name, mail, password, driver):
        self.tenant_name = tenant_name
        self.mail = mail
        self.password = password
        self.driver = driver

    def customerAdd(self):
        try:
            #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h4[contains(text()='"+self.tenant_name+"'")))
            #self.driver.find_element(By.XPATH, "//h4[contains(text(), '"+self.tenant_name+"')]").click()
            add_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'add-new-item-btn')]")))
            add_button.click()
            time.sleep(1)

        except Exception as e:
            print(e)

    def customerCreate(self):
        #global customer_data
        self.driver.implicitly_wait(10)
        #print(len(customer_data["Name"]))
        for i in range(0, (len(customer_data["Name"]))):
            CustomerPage.customerAdd(self)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Add Customer']")))
            self.driver.find_element(By.NAME, "businessName").send_keys(customer_data["Name"][i])
            self.driver.find_element(By.NAME, "businessTheme").send_keys(customer_data["Theme"][i])
            self.driver.find_element(By.NAME, "url").send_keys(customer_data["URL"][i])
            self.driver.find_element(By.NAME, "description").send_keys(customer_data["Description"][i])
            self.driver.find_element(By.XPATH, "//div[contains(@class, 'css-nwjfc')]").click()
            time.sleep(1)
            template_name = customer_data['Template'][i]
            print(template_name)
            self.driver.find_element(By.XPATH, f"//div[contains(text(), '{template_name}')]").click()
        #time.sleep(5)
            self.driver.find_element(By.NAME, "locationAddress").send_keys(customer_data['Address'][i])
            location = self.driver.find_element(By.XPATH,"//label[text()='Location']/following::input[1]")
            location.send_keys(customer_data['Location'][i])
            time.sleep(1)
            countries = self.driver.find_elements(By.XPATH, "//div[contains(@class,'option')]")
            print(len(countries))
            for country in countries:
                if country.text == customer_data['Location'][i]:
                    country.click()
                # time.sleep(2)
                    break
            logo_file = os.path.abspath(customer_data["Logo"][i])
            self.driver.find_element(By.XPATH, "(//input[@type='file'])[1]").send_keys(logo_file)
            image_file = os.path.abspath(customer_data["Image"][i])
            self.driver.find_element(By.XPATH, "(//input[@type='file'])[2]").send_keys(image_file)
            time.sleep(1)
            self.driver.find_element(By.XPATH, "//button[text()='Add']").click()
            time.sleep(2)

    def customerAccount(self, tenant_name):
        mail_address = []
        self.driver.find_element(By.XPATH, "//li[@class='user-btn']").click()
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h4[text()='Users']")))
        #customer_data = readfile.read_file()
        for customer in customer_data["Name"]:
            self.driver.find_element(By.XPATH, "//button[contains(@class, 'form-item')]").click()
            time.sleep(1)
            self.driver.find_element(By.NAME, "name").send_keys(customer)
            mail = str(customer).replace(" ","").lower() + "@mailinator.com"
            print(mail)
            mail_address.append(mail)
            self.driver.find_element(By.NAME, "userEmail").send_keys(mail)
            self.driver.find_element(By.XPATH, "//label[text()='Tenant']/following::div[contains(@class, 'css-nwjfc')][1]").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, f"//div[contains(text(),'{tenant_name}')]").click()
            time.sleep(1)
            self.driver.find_element(By.XPATH,
                                     "//label[text()='Customer']/following::div[contains(@class, 'css-nwjfc')][1]").click()
            self.driver.find_element(By.XPATH, f"//div[contains(text(),'{customer}')]").click()
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(2)
        return mail_address
            #self.driver.find_element(By.XPATH, "(//button[contains(@class, 'btn close-side-panel-btn')])[1]").click()

    def customerDelete(self):
        #customer_data = readfile.read_file()
        self.driver.find_element(By.XPATH, "//li[@class='dashboard-btn']").click()
        time.sleep(2)
        #customers = ["Customer 2", "Customer 3", "Customer 4", "Customer 5"]
        for customer in customer_data["Name"]:
            self.driver.find_element(By.XPATH, f"//h4[text()='{customer}']/following::button[1]").click()
            self.driver.find_element(By.LINK_TEXT, "Delete").click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='message-block']")))
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//button[text()='Ok']").click()
            time.sleep(2)



if __name__ == "__main__":
    customercred_dict = {}
    tacred_dict = {}
    tenant_name = "Tenant BCA"
    #ta_mail = "tenantbca0@mailinator.com"
    #user_password = "12346"
    #Login_class(name=ta_mail, password=user_password).Login_fuction()
    login_obj = Login_class(name="platform-owner@cosmicnode.com", password="dUOktEGlWaWj_EIzumoiH#")
    login_obj.Login_fuction()
    #tenant = self.driver.find_element(By.XPATH, "(//h4[contains(@class,'m-0')])[1]").text
    #if tenant_name == tenant
    tenant_obj = Tenant(tenant_name, driver=Login_class.driver)
    tenant = login_obj.driver.find_element(By.XPATH, "(//h4[contains(@class,'m-0')])[1]").text
    if tenant_name == tenant:
        tenant_obj.tenant_delete()
    tenant_obj.tenant_create()
    user_mail = tenant_obj.tenantadmin_create()

    user_username = (user_mail.split("@"))[0]
    #print(user_username, user_mail)
    mailinator_obj = Mailinator("12345", driver=tenant_obj.driver)
    mailinator_obj.user_invite(user_username)
    user_password = mailinator_obj.user_setcredentials()
    tacred_dict[user_mail] = user_password
    print(f"credentials of the tenant admin is {tacred_dict}")
    cust_obj = Customer(tenant_name= tenant_name, mail=user_mail, password=user_password, driver=tenant_obj.driver)
    cust_obj.ta_logout()
    Login_class(name=user_mail, password=user_password).Login_fuction()

    #cust_obj = Customer(tenant_name=tenant_name, mail=ta_mail, password=user_password, driver=tenant_obj.driver)
    cust_obj.Customer_Add()
    cust_obj.Customer_Create()
    customer_mails = cust_obj.customer_account(tenant_name)
    #customer_mails = ["customer2@mailinator.com", "customer3@mailinator.com", "customer4@mailinator.com", "customer5@mailinator.com"]
    for mail in customer_mails:
        username = mail.split("@")
        mailinator_obj.user_invite(username[0])
        password = mailinator_obj.user_setcredentials()
        customercred_dict[mail] = password
    print(f"customer credentials are {customercred_dict}")
    cust_obj.customer_delete()




