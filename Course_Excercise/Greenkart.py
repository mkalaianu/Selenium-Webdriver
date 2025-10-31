import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

Exp_list = ["Cauliflower", "Carrot", "Capsicum", "Cashews"]
actual_list = []
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ca")
time.sleep(2)
# get the child element from parent element
product_list = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(product_list))
for product in product_list:
    item_name = (product.find_element(By.XPATH, "h4").text).split("-")
    actual_list.append(item_name[0].strip())
    product.find_element(By.XPATH, "div/button").click()
time.sleep(2)
print(actual_list)
assert Exp_list == actual_list

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//div/button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)

sum = 0
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
for price in prices:
    sum += int(price.text)

print(sum)
total_amt = driver.find_element(By.CSS_SELECTOR, ".totAmt").text
#print(int(total_amt))
assert sum == int(total_amt)
discount_amt = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
assert sum > float(discount_amt)




