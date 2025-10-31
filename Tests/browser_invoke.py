import time
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service

#service_obj = Service("..//Browser_Driver/chromedriver-win64/chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome()
driver.get("https://staging-infinity.cosmicnode.com")
print(driver.title)
print(driver.current_url)
time.sleep(5)

service_obj = Service("..//Browser_Driver/edgedriver_win64/msedgedriver.exe")
driver1 = webdriver.Edge(service=service_obj)
#driver1 = webdriver.Edge()
driver1.get("https://staging-infinity.cosmicnode.com")
print(driver1.title)
print(driver1.current_url)
time.sleep(5)


