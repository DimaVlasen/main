#from FinalProject 
import data
import xlsxwriter

title_list = ['Код валюти', 'Рік', 'Курс на 1.10', 'Курс на 1.11',
              'Курс на 1.12',
              'Курс на 1.12 курс крб.',
              'Курс на 1.12 рівень',
              'Рівень за три місяці']

workbook = xlsxwriter.Workbook('table_efficiency_of_enterprise.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True, })
bold.set_text_wrap()
bold.set_align('center')
bold.set_align('top')
bold.set_border()
border = workbook.add_format()
border.set_border()

for index, title in enumerate(title_list):
    worksheet.set_column(0, index, 15)
    worksheet.write(0, index, title, bold)

for row_id, enterprise in enumerate(data.sorted_enterprise_efficiency_list):

    column = 0
    for attr, value in vars(enterprise).items():
        worksheet.write(row_id + 1, column, value, border)
        column += 1

workbook.close()