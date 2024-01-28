from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Index.html")

# //input[@placeholder='First Name']
#
#
# //input[@placeholder='First Name' and @type='text']
# //input[@placeholder='First Name' or @type='text']
#
# # using text()
# //label[text()='Full Name* ']
#
# # using contains to find text
# //label[contains(text(), 'Full N')]
#
# # for child , parent and ancestors
# //form[@id='basicBootstrapForm']/child::div
# //form[@id='basicBootstrapForm']/parent::div
# //form[@id='basicBootstrapForm']/ancestor::div
#
# # for following and preceding sibilings
# //input[@id='checkbox1']/following-sibling::label
# //label[@class='checks']/preceding-sibling::input

#Example of xpath :

driver.find_element(By.ID, "email").send_keys("test@gmail.com")
driver.find_element(By.ID, "enterimg").click()
driver.find_element(By.XPATH, "//input[@type='radio' and @value='Male']").click()

# example of exacting the value
list1 = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for ele in list1:
    val = ele.get_attribute("value")
    print(val)
    if val == 'Cricket':
        ele.click()

