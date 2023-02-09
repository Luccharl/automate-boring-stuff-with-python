import ezsheets

wb1 = ezsheets.Spreadsheet('11yxtvLuFRxK7AILg_2IPtiOaWhznn9ogB8CpnjmDxNM')
sheet1 = wb1[0]
num = ezsheets.getColumnNumberOf('B')
col1 = sheet1.getColumn(num)

for email in col1:
    if email.endswith('.com'):
        print(email)