import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://magento.softwaretestingboard.com/")
driver.maximize_window()
driver.implicitly_wait(3)

women = driver.find_element(By.ID, "ui-id-4")
action = ActionChains(driver)

action.move_to_element(women).perform()
time.sleep(3)

top = driver.find_element(By.ID, "ui-id-9")
action.move_to_element(top).perform()
time.sleep(3)

driver.find_element(By.ID, "ui-id-11").click()
time.sleep(3)

driver.find_element(By.ID, "search").click()

action.key_down(Keys.SHIFT).send_keys("olivia").send_keys(Keys.ENTER).perform()
time.sleep(2)
