import json
import sys
import time

import pytest
from selenium.webdriver.common.by import By
import os.path
from selenium.common.exceptions import StaleElementReferenceException
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from Page_Object.Login import Login_page
from Page_Object.Mailinator import MailinatorPage
from Page_Object.Customer import CustomerPage


# remove the error no module called
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


data_filepath = os.path.abspath("../files/test_e2e.json")
with open(data_filepath) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    tenant_name = test_list_item["tenant_name"]
    customercred_dict = {}
    tacred_dict = {}
    driver = browserInstance

    login_pageobj = Login_page(driver, test_list_item["user_name"], test_list_item["password"], test_list_item["url"])
    tenantpage_obj = login_pageobj.Login()
    tenant_list = driver.find_elements(By.TAG_NAME, "h4")
    for tenant in tenant_list:
        if tenant_name == tenant.text:
            tenantpage_obj.tenantDelete(tenant_name)
            break

    tenantpage_obj.tenantCreate(tenant_name)
    user_mail = tenantpage_obj.tenantAdminCreate()
    user_username = (user_mail.split("@"))[0]
    mailinator_obj = MailinatorPage(test_list_item["ta_password"], driver)
    mailinator_obj.userInvite(user_username)
    user_password = mailinator_obj.userSetCredentials()
    tacred_dict[user_mail] = user_password
    tenantpage_obj.tenantLogout()
    print(f"credentials of the tenant admin is {tacred_dict}")
    cust_obj = CustomerPage(tenant_name=tenant_name, mail=user_mail, password=user_password, driver=driver)
    Login_page(driver, user_mail, user_password, test_list_item["url"]).Login()
    # cust_obj = Customer(tenant_name=tenant_name, mail=ta_mail, password=user_password, driver=tenant_obj.driver)
    cust_obj.customerCreate()
    customer_mails = cust_obj.customerAccount(tenant_name)
    # customer_mails = ["customer2@mailinator.com", "customer3@mailinator.com", "customer4@mailinator.com", "customer5@mailinator.com"]
    for mail in customer_mails:
        username = mail.split("@")
        mailinator_obj.userInvite(username[0])
        password = mailinator_obj.userSetCredentials()
        customercred_dict[mail] = password
    print(f"customer credentials are {customercred_dict}")
    cust_obj.customerDelete()


