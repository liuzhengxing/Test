# encoding: utf-8

from selenium import webdriver
import time
import random

class PublicMethod():

    def openBrowser(self):
        self.browser = webdriver.Chrome()
        self.url = "http://192.168.138.191:9080/neusoftEEP_web"
        self.browser.get(self.url)

    def getObject(self, xpath):
            return self.browser.find_element_by_xpath(xpath)

    def getObjects(self,xpath):
            return self.browser.find_elements_by_xpath(xpath)

    def login(self):
        self.browser.find_element_by_id("userName").send_keys("yy")
        self.browser.find_element_by_id("password").send_keys("123456")
        self.getObject("//button").click()
        time.sleep(3)
        self.browser.maximize_window()


    def logOut(self):
        # self.getObject('//*[@id="app"]/div/div/div[1]/div[2]/div[2]/ul/li[3]/a').click()
        # time.sleep(3)
        self.browser.quit()





