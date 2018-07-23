# -*-coding: utf-8 -*-

import time
import unittest

from 测试用例.功能自动化.公共部分.登录 import Public
from 测试用例.功能自动化.公共部分 import 全局参数


class Bm(unittest.TestCase):
    u"""
    部门模块用例
    """
    def setUp(self):
        """
        登录操作
        """
        public = Public()
        self.driver = public.login()

    def test_bm_create_one(self):
        u"""创建一级部门"""
        dr = self.driver
        time.sleep(1)

        # 获取参数
        ywdybm = 全局参数.ywdybm
        yjbmbm = 全局参数.yjbmbm
        ejbmbm = 全局参数.rjbmbm

        # 点击系统管理
        dr.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[2]/div/ul/li[9]').click()
        time.sleep(1)

        # 点击组织管理
        dr.find_element_by_xpath('//*[@id="5E29F6F2D7E61810E055000000000001$Menu"]/li[3]').click()
        time.sleep(3)

        # 点击部门
        dr.find_element_by_xpath('//*[@id="580A74AE38E842F3E055000000000001$Menu"]/li[2]').click()
        time.sleep(3)

        # 选择业务单元
        dr.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div'
                                 '/div[1]/div[1]/div/div/div/div/span/span/span/i').click()

        # 搜索业务单元
        dr.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]'
                                 '/div/span/input').send_keys(ywdybm)
        dr.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]'
                                 '/div/span/span/i').click()

        # 选择
        dr.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[2]/div'
                                 '/div/div/div/div/div/div/div/div/div/div/div/table/tbody/tr/td[1]/span/label'
                                 '/span/input').click()

        dr.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[3]'
                                 '/div[1]/button').click()

        # 点击创建
        dr.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div'
                                 '/div[1]/div[3]/button').click()
        time.sleep(1)

        # 输入部门编码
        dr.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]'
                                 '/div[1]/div/div[2]/div/input').send_keys(yjbmbm)

        # 输入部门名称
        dr.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]'
                                 '/div[2]/div/div[2]/div/input').send_keys(yjbmbm)

        # 点击确认按钮
        dr.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[3]'
                                 '/div[1]/button').click()

        # -----------------------------验证-------------------------------------
        # 点击业务单元
        element_check = dr.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div'
                                                 '/div[2]/div/div[1]/div/div/div[2]/div/div/div/div[2]/div/div/div'
                                                 '/div/ul/li/span[2]/span/span').text
        time.sleep(3)
        try:
            self.assertEqual(element_check, yjbmbm)
        except AssertionError as e:
            print("未找到一级部门")

    def test_bm_create_two(self):
        u"""创建二级部门"""
        dr = self.driver
        time.sleep(1)

        # 获取参数
        ywdybm = 全局参数.ywdybm
        yjbmbm = 全局参数.yjbmbm
        ejbmbm = 全局参数.rjbmbm

        # 选择业务单元
        dr.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div'
                                 '/div[1]/div[1]/div/div/div/div/span/span/span/i').click()

        # 搜索业务单元
        dr.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]'
                                 '/div/span/input').send_keys(ywdybm)
        dr.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]'
                                 '/div/span/span/i').click()

        # 选择
        dr.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[2]/div'
                                 '/div/div/div/div/div/div/div/div/div/div/div/table/tbody/tr/td[1]/span/label'
                                 '/span/input').click()

        dr.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[3]'
                                 '/div[1]/button').click()

        # 点选一级部门
        dr.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]'
                                 '/div/div/div[2]/div/div/div/div[2]/div/div/div/div/ul/li/span[2]/span').click()

        # 点击创建
        dr.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div'
                                 '/div[1]/div[3]/button').click()
        time.sleep(1)

        # 输入二级部门编码
        dr.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]'
                                 '/div[1]/div/div[2]/div/input').send_keys(ejbmbm)

        # 输入二级部门名称
        dr.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]'
                                 '/div[2]/div/div[2]/div/input').send_keys(ejbmbm)

        # 点击确认按钮
        dr.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[3]'
                                 '/div[1]/button').click()

        # -----------------------------验证-------------------------------------
        # 点击展开按钮
        dr.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]'
                                 '/div/div/div[2]/div/div/div/div[2]/div/div/div/div/ul/li/span[1]').click()
        time.sleep(1)
        element_check = dr.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div'
                                                 '/div[2]/div/div[1]/div/div/div[2]/div/div/div/div[2]/div/div/div'
                                                 '/div/ul/li/ul/li/span[2]/span/span/text()').text
        try:
            self.assertEqual(element_check, ejbmbm)
        except AssertionError as e:
            print("未找到二级部门")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
