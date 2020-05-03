# 程序作用：打开当前文件夹下的excel文件；逐个分析excel文件并进行编辑；汇总生成新excel文件为"汇总excel.xlsx"
#（未解决问题：表格内时间格式转换不正确）
#2020年4月25日
#python  3.72

import os, time, datetime
import xlrd, xlwt

'''筛选excel文件，以 .xlsx 作为判断'''
workbook_1 = xlwt.Workbook()
worksheet = workbook_1.add_sheet('汇总表')

n = 0
# m = 0
for fname in os.listdir('./'):      #遍历当前文件夹内所有文件，含隐藏文件
    if '.xls' in fname:
        workbook = xlrd.open_workbook(fname)    #打开遍历到的第1个excel文件
        sheet = workbook.sheet_by_index(0)

        for row in range(0, sheet.nrows):
            for col in range(0, sheet.ncols):
                # print(row, col)
                data = sheet.cell_value(row, col)
                if col == 0 and type(data) != str:
                    data1 = int(data) + 18298
                    struct_time = datetime.datetime.fromtimestamp(data1)
                    worksheet.write(n + row, col, struct_time)
                else:
                    worksheet.write(n + row, col, data)
        n = n + sheet.nrows
        print(f'{fname}已操作完成！\n表格名称：{sheet.name}, 行数： {sheet.nrows}，列数： {sheet.ncols}')

workbook_1.save('汇总excel.xlsx')
