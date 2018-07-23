# encoding: utf-8

from selenium import webdriver
import time
import xlrd

fname = 'E:\\WebAuto\\Data_基本信息 _物料信息.xlsx'
bk = xlrd.open_workbook(fname,"rb")
sh = bk.sheet_by_name("material")

url = sh.cell_value(1,1)
browser = webdriver.Chrome()
browser.get(url)


