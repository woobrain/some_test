# coding = utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
browser.maximize_window()
print([browser.title,browser.current_url])
browser.find_element_by_id("kw").send_keys("selenium\n")
time.sleep(5)
# browser.find_element_by_id("su").click()
print([browser.title,browser.current_url])
time.sleep(5)
browser.find_element_by_xpath("//*[@id='2']/h3/a").click()
time.sleep(5)
browser.switch_to.window(browser.window_handles[-1])
print([browser.title,browser.current_url])


# browser.close()