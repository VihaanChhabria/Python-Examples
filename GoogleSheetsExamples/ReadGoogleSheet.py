import gspread
import time

saLocation = r"C:\Users\vihaa\Python-Examples\GoogleSheetsExamples\service_account.json"

sa = gspread.service_account(saLocation)
sh = sa.open("Test Sheet")

wks = sh.worksheet("Sheet1")

print('Rows: ', wks.row_count)
print('Cols: ', wks.col_count)

#print(wks.acell('A9').value)
#print(wks.cell(3, 4).value)
print(wks.get('A7:E9'))

#print(wks.get_all_records())
#print(wks.get_all_values())

#wks.update('A3', 'Anthony')
#wks.update('D2:E3', [['Engineering', 'Tennis'], ['Business', 'Pottery']])
#wks.update('F2', '=UPPER(E2)', raw=False)

#wks.delete_rows(25)

print(wks.cell(1, 1))