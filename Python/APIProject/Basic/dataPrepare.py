# encoding: utf-8

import xlrd

workbook = xlrd.open_workbook('E:\\APITesting\\APITestData.xlsx')


class dev():
    worksheet = workbook.sheet_by_name('dev')

    url_Create = worksheet.cell_value(0,1)
    url_Delete = worksheet.cell_value(1,1)

class sit():
    print("waiting")

