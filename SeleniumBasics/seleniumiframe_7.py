from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

#iframe by index
driver.switch_to.frame(0)

#iFrame by name and ID
driver.switch_to.frame("singleframe")
driver.switch_to.frame("SingleFrame")

#iFrame by xpath
single_frame = driver.find_element(By.XPATH, "//div[@id='Single']/iframe")
driver.switch_to.frame(single_frame)
driver.find_element(By.TAG_NAME, "input").send_keys("Hi am i Frame")

#to get outside the iframe
driver.switch_to.default_content()