# -*-coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import *


class Public():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://192.168.138.54:9080/neusoftEEP_web')

    def login(self):
        dr = self.driver

        # 输入用户名、密码，登录
        dr.find_element_by_xpath('//*[@id="userName"]').send_keys('QU000')
        dr.find_element_by_xpath('//*[@id="password"]').send_keys('1')
        dr.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[3]/div/div/button').click()
        time.sleep(2)

        # 选择业务组
        element_ywz = dr.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/div[2]/ul/li[2]/div/span')
        chain = ActionChains(dr)
        chain.move_to_element(element_ywz).perform()
        time.sleep(1)
        dr.find_element_by_xpath('//*[@id="group$Menu"]/li[4]').click()


        # 选择方案
        element_fa = dr.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/div[2]/ul/li[1]/div/span')
        chain.move_to_element(element_fa).perform()
        time.sleep(1)
        dr.find_element_by_xpath('//*[@id="scheme$Menu"]/li[2]').click()

        # 返回driver后续引用
        return dr


if __name__ == '__main__':
    p = Public()
    p.login()

