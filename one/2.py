from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.get("http://www.baidu.com")
# wd.execute_script('alert("ok")')
print(wd.find_element(By.ID, 'su').get_attribute('id'))
print(wd.find_element_by_id('su').location)