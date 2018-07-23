# encoding: utf-8

from selenium import webdriver
import time
import random

browser = webdriver.Chrome()
url = "http://192.168.138.132/neusoftEEP_web/login"

browser.get(url)
time.sleep(3)

def getObject(xpath):
    return browser.find_element_by_xpath(xpath)

def getObjects(xpath):
    return browser.find_elements_by_xpath(xpath)

def login():
    browser.find_element_by_id("userName").send_keys("admin")
    browser.find_element_by_id("password").send_keys("123456")
    getObject("//button").click()
    time.sleep(3)
    browser.maximize_window()

def createMaterial():
    getObject('//span[contains(text(),"基本信息")]').click()
    time.sleep(3)
    getObject('//span[contains(text(),"物料信息")]').click()
    time.sleep(3)
    getObject('//span[contains(text(),"物料分类")]/..').click()
    time.sleep(3)

    getObject('//span[contains(text(),"创 建")]/..').click()
    time.sleep(3)

    getObjects('(//input[@name="code"])')[1].send_keys('0706' + str(random.randint(1, 1000)))
    time.sleep(3)
    getObjects('(//input[@name="name"])')[1].send_keys('test')
    time.sleep(3)
    getObjects('//i[@class = "anticon anticon-search find-back-icon-search"]')[1].click()
    time.sleep(3)
    getObjects('//input[@class = "ant-radio-input"]')[0].click()
    getObject('//span[contains(text(),"确 定")]/..').click()
    time.sleep(3)
    getObject('//span[contains(text(),"确 认")]/..').click()
