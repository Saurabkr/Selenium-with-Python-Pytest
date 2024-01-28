import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

#time.sleep -> stops python for few second which is given
#implicitwait :


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Index.html")
driver.maximize_window()
driver.implicitly_wait(4)

driver.find_element(By.ID, "email").send_keys("test@gmail.com")
driver.find_element(By.ID, "enterimg").click()


wait = WebDriverWait(driver, 4).until(
     EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='First Name']"))
)
wait.send_keys("Saurab")

driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Kumar")

time.sleep(4)







