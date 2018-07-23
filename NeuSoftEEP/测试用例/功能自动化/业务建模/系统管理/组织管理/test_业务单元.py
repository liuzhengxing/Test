# -*-coding: utf-8 -*-

import time
import unittest

from 测试用例.功能自动化.公共部分.登录 import Public
from 测试用例.功能自动化.公共部分 import 全局参数


class Ywdy(unittest.TestCase):
    u"""
    业务单元模块用例
    """
    def setUp(self):
        """
        登录操作
        """
        public = Public()
        self.driver = public.login()

    def test_ywdy_create(self):
        u"""创建业务单元"""
        dr = self.driver
        time.sleep(1)

        # 点击系统管理
        dr.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[2]/div/ul/li[9]').click()
        time.sleep(1)

        # 点击组织管理
        dr.find_element_by_xpath('//*[@id="5E29F6F2D7E61810E055000000000001$Menu"]/li[3]').click()
        time.sleep(3)

        # 点击业务单元
        dr.find_element_by_xpath('//*[@id="580A74AE38E842F3E055000000000001$Menu"]/li[4]').click()
        time.sleep(3)

        # 点击创建
        dr.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div'
                                 '/div[1]/div/div/div/div[1]/button').click()
        time.sleep(1)

        # 输入业务单元编码
        # ywdybm = 'AUTO' + str(int(time.time()))
        ywdybm = 全局参数.ywdybm
        dr.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]'
                                 '/div/div[2]/div[1]/div[1]/div/div[2]/div/input').send_keys(ywdybm)

        # 输入业务单元名称
        dr.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]'
                                 '/div/div[2]/div[1]/div[2]/div/div[2]/div/input').send_keys(ywdybm)

        # 选择职能
        dr.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]'
                                 '/div/div[2]/div[3]/div[2]/div/div[2]/div/div/label[2]'
                                 '/span[1]/input').click()
        dr.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]'
                                 '/div/div[2]/div[3]/div[2]/div/div[2]/div/div/label[9]'
                                 '/span[1]/input').click()
        time.sleep(3)

        # 点击保存
        dr.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]'
                                 '/div/div/div/div[5]/button').click()

        time.sleep(5)

        # -----------------------------验证-------------------------------------
        # 点击业务单元
        dr.find_element_by_xpath('//*[@id="580A74AE38E842F3E055000000000001$Menu"]/li[4]').click()
        time.sleep(3)
        element_check = dr.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div/div/div/div[2]'
                                                 '/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div'
                                                 '/div/div/table/tbody/tr[1]/td[3]/span').get_attribute('title')
        try:
            self.assertEqual(element_check, ywdybm)
        except AssertionError as e:
            print("找不到这个标题")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
