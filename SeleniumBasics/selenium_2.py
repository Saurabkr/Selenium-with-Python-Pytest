from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com/")

driver.find_element(By.LINK_TEXT, "About").click()
driver.find_element((By.PARTIAL_LINK_TEXT, "How")).click()
driver.quit()

