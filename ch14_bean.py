import ezsheets

ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
sheet1 = ss[0]
row_count = sheet1.rowCount
#col_count = sheet1.columnCount


for i in range(2, row_count+1):
    try: 
        if int(sheet1.getRow(i)[0]) * int(sheet1.getRow(i)[1]) == int(sheet1.getRow(i)[2]):
            continue
            #print(str(i) + ' : ' + str(int(sheet1.getRow(i)[0]) * int(sheet1.getRow(i)[1])))
        else:
            print(f'Row {i} has an incorrect total')
    except ValueError:
        continue