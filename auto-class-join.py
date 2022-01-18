import selenium
import datetime
import time
from selenium import webdriver
driver = webdriver.Chrome(
    executable_path='D:\\Python\\chromedriver_win32\\chromedriver.exe')
minutes = int(datetime.datetime.now().minute)
hour = int(datetime.datetime.now().hour)
driver.maximize_window()
driver.get("https://rkmvdeoghar.myperfectice.com/")
login = driver.find_element_by_xpath(
    '//*[@id="wrapper"]/div/div[1]/div[2]/div/button')
time.sleep(2)
login.click()
time.sleep(2)
username = driver.find_element_by_xpath(
    '//*[@id="page-wrapper"]/div/div/div/form/div/div/div/div[2]/input')
username.send_keys("dilipkumarmishra74@gmail.com")
password = driver.find_element_by_xpath('//*[@id="userpass"]')
password.send_keys("AmanKumar17")
button1 = driver.find_element_by_xpath(
    '//*[@id="page-wrapper"]/div/div/div/form/div/div/div/button')
button1.click()
time.sleep(3)
classroom = driver.find_element_by_xpath(
    '//*[@id="main-menu"]/ng-include/ul/li[3]/a/span')
classroom.click()
time.sleep(3)
class_10 = driver.find_element_by_xpath(
    '//*[@id="mCSB_12_container"]/ul/li[2]')
class_10.click()
time.sleep(2)
join_sessions = driver.find_element_by_xpath('')
join_sessions.click()
time.sleep(2)
