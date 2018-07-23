# encoding: utf-8

l = [[1,2,3,4,5,6]]
print(l[0])


import xlrd



#定义excel文件地址
fname = 'C:\\Users\\admin\\Desktop\\material.xlsx'
bk = xlrd.open_workbook(fname,"rb")
sh = bk.sheet_by_name("material")

#sheet页的行数和列数
nrows = sh.nrows
nclos = sh.ncols


#循环读取每一行的数据并写入到list中

for i in range(1,nrows):
    row_data = sh.row_values(i)
    print(row_data[0],row_data[1])
