from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass

signin= "ktroupe@sfo.yearup.org"

password = getpass.getpass("Enter your password: ")

driver = webdriver.Chrome()
driver.get ("http://www.schoology.com/")
time.sleep(3)
driver.find_element_by_id("login-header").click()
driver.find_element_by_xpath("//*[@id='edit-mail']").send_keys(signin)
driver.find_element_by_id("edit-pass").send_keys(password)

driver.find_element_by_class_name("form-submit").click()
