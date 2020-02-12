import tabula
inputPDF = 'dfb13.pdf'

df = tabula.read_pdf(inputPDF)
print('\nTable from PDF file\n'+str(df))
PDF_T_CSV = '/Users/300262/PycharmProjects/Python-course/PDF_T_CSV1.csv'
PDF_T_EXCEL = '/Users/300262/PycharmProjects/Python-course/PDF_T_EXCEL.xlsx'

tabula.convert_into(inputPDF, PDF_T_CSV, output_format='csv', pages='all')
print('\nSUCCESSFULY CONVERTED INTO CSV FILE')

