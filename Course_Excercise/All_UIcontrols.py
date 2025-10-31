import time

from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("start-maximized")
chrome_option.add_argument("--ignore-certificate-errors")
#chrome_option.add_argument("headless")

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)


# Java script handle
driver.execute_script("window.scrollBy(0, 500)")


# checking the Header text
heading_text = driver.find_element(By.XPATH, "//h1[text()='Practice Page']").text
print(heading_text)
assert (heading_text == "Practice Page")
#time.sleep(2)

# selecting the Radio button
driver.find_element(By.NAME, "radioButton").click()
#time.sleep(2)

radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
for radio_button in radio_buttons:
    if radio_button.get_attribute("value") == "radio2":
        radio_button.click()
        assert radio_button.is_selected()
        #time.sleep(2)
        break

# Dynamic dropdown
driver.find_element(By.CSS_SELECTOR, "#autocomplete").send_keys("Ne")
time.sleep(1)
countries = driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item")
print(len(countries))
for country in countries:
    if country.text == "Netherlands":
        country.click()
        break
time.sleep(1)
country_name = driver.find_element(By.CSS_SELECTOR, "#autocomplete").get_attribute("value")
print(country_name)
assert "Netherlands" in country_name

# selecting the value from static dropdown
dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))
dropdown.select_by_index(1)
#time.sleep(1)
dropdown.select_by_visible_text("Option2")
#time.sleep(1)
dropdown.select_by_value("option3")
time.sleep(2)

#Selecting the check box
checkbox_options = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
print(len(checkbox_options))
for option in checkbox_options:
    if option.get_attribute("value") == "option3":
        option.click()
        #time.sleep(2)
        break

# Text Hide and show
driver.find_element(By.ID, "displayed-text").send_keys("mani")
assert driver.find_element(By.ID, "displayed-text").is_displayed()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#hide-textbox").click()
time.sleep(2)
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

# HAndle the brower alerts or java script alerts
driver.find_element(By.NAME, "enter-name").send_keys("Mani")
#time.sleep(1)
driver.find_element(By.ID, "alertbtn").click()
time.sleep(2)
alerts = driver.switch_to.alert
print(alerts.text)
assert "Mani" in alerts.text
alerts.accept()
time.sleep(3)

driver.find_element(By.ID, "confirmbtn").click()
time.sleep(2)
alerts = driver.switch_to.alert
alerts.dismiss()

# Switch window and tab
driver.find_element(By.ID, "openwindow").click()
openedwindows = driver.window_handles
driver.switch_to.window(openedwindows[1])
print(driver.find_element(By.XPATH, "//li[.='info@qaclickacademy.com']").text)
driver.switch_to.window(openedwindows[0])
time.sleep(2)
#Tab
driver.find_element(By.ID, "opentab").click()
openedwindows = driver.window_handles
driver.switch_to.window(openedwindows[1])
print(driver.find_element(By.XPATH, "//li[.='info@qaclickacademy.com']").text)
driver.switch_to.window(openedwindows[0])
time.sleep(2)

# special mouse actions --- Actions chain
chain = ActionChains(driver)
chain.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
#chain.drag_and_drop()
#chain.click_and_hold()
chain.double_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
time.sleep(2)
chain.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
chain.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
time.sleep(2)

# iframes
driver.switch_to.frame("courses-iframe")
driver.find_element(By.LINK_TEXT,"Courses").click()
time.sleep(2)
driver.switch_to.default_content()

#   Sorting the web tables
browser_list = []
name_person = driver.find_elements(By.XPATH, "//div[@class='tableFixHead']/table/tbody/tr/td[1]")
for name in name_person:
    browser_list.append(name.text)
print(browser_list)
copy_browserlist = browser_list.copy()
#print(copy_browserlist)
copy_browserlist.sort()
#sorted_list = sorted(copy_browserlist)
print(copy_browserlist)

assert browser_list == copy_browserlist













