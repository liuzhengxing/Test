# encoding: utf-8

import xlrd

workbook = xlrd.open_workbook('C:\\Users\\admin\\Desktop\\material.xlsx')
worksheet = workbook.sheet_by_name('material')

#sheet页的行数和列数
nrows = worksheet.nrows
nclos = worksheet.ncols
list = []
def getData():
    for i in range(1, nrows):
        for j in range(0, 2):
            data = worksheet.cell_value(i,j)
            list.append(data)
    return list


Data1 = getData()
print(Data1)


#循环读取每一行的数据并写入到list中

def getData1():
    for i in range(1,nrows):
        row_data = worksheet.row_values(i)
        print(row_data[0],row_data[1])