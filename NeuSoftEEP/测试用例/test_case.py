# -*-coding=utf-8 -*-

import os
import unittest

from public import params

# 列出某个文件夹下的所有 case,这里用的是 python，
# 所在 py 文件运行一次后会生成一个 pyc 的副本
Top_Level_Dir = params.BaseDir + '\\测试用例'
# CaseDir1 = Top_Level_Dir + '\\功能自动化'
CaseDir2 = Top_Level_Dir + '\\接口自动化_V2'

CaseDirs=[]
# CaseDirs.append(CaseDir1)
CaseDirs.append(CaseDir2)


def creatsuite():
    testunit = unittest.TestSuite()

    # discover 方法定义
    for CaseDir in CaseDirs:
        discover = unittest.defaultTestLoader.discover(start_dir=CaseDir, pattern='test*.py',
                                                       top_level_dir=Top_Level_Dir)
        # print(discover)

        # discover 方法筛选出来的用例，循环添加到测试套件中
        for test_suite in discover:
            for test_case in test_suite:
                testunit.addTests(test_case)
    print(testunit)
    return testunit


if __name__ == '__main__':
    # creatsuite()
    print(Top_Level_Dir)
    print(CaseDir2)