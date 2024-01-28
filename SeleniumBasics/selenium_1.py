from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Index.html")

driver.find_element(By.ID, "email").send_keys("test@gmail.com")
driver.find_element(By.ID, "enterimg").click()

driver.quit()