from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()

parent = driver.current_window_handle
print(parent)

driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']").click()

windows = driver.window_handles

for window in windows:
    if window != parent:
        driver.switch_to.window(window)


driver.find_element(By.XPATH, "//a[@href='/downloads']").click()

driver.close() #to close particular working tab
