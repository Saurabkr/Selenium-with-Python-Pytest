from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Register.html")
print(driver.current_url)
# driver.maximize_window()
dropDown = driver.find_element(By.ID, "Skills")
Select(dropDown).select_by_index(5)
Select(dropDown).select_by_value("HTML")
Select(dropDown).select_by_visible_text("Android")
# driver.implicitly_wait(3000)

#To open new link
driver.get("https://www.google.com/")
print(driver.current_url)
driver.back()
driver.refresh()
driver.forward()
driver.quit()
