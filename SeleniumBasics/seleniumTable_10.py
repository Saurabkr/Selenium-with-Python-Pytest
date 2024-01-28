import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.redbus.in/")
driver.maximize_window()

# date = "29-01-2024"
# dates = date.split("-")

driver.find_element(By.CLASS_NAME, "dateText").click()
time.sleep((3))

driver.find_element(By.XPATH, "//div[@id='onwardCal']//text[2]").click()



