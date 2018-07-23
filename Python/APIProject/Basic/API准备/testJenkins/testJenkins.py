# encoding: utf-8
import os

path = "C:\\Users\\admin\\PycharmProjects\\APIProject\\Basic\\API准备\\testJenkins"
# path = os.getcwd()---获取当前工作路径

print(path)

file = os.listdir(path)

print(file)

for c in file:
    if c.endswith('.py') and c.find("testJenkins")==-1:    #去掉AllTest.py文件
        print(c)
        os.system(os.path.join(path,c))