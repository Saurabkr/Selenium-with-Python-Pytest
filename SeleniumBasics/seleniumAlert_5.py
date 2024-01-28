from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()

#Accept
driver.find_element(By.ID, "OKTab").click()
# driver.sleep(2)
driver.switch_to.alert.accept()
# driver.sleep(2)

#Cancel
driver.find_element(By.XPATH, "//a[@href='#CancelTab']").click()
driver.find_element(By.ID, "CancelTab").click()
# driver.sleep(2)
driver.switch_to.alert.dismiss()
# driver.sleep(2)

#Read or write text in alert
driver.find_element(By.XPATH, "//a[@href='#Textbox']").click()
driver.find_element(By.ID, "Textbox").click()
# driver.sleep(2)
txt = driver.switch_to.alert.text
print(txt)
driver.switch_to.alert.send_keys("HI i am saurab")
driver.Sleep(2)
driver.switch_to.alert.accept()

driver.quit()



