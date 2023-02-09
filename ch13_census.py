#! python 3

import openpyxl,pprint

print('Opening Workbook')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.active
county_data = {}

print('reading rows...')
for row in range(2, sheet.max_row+1):
    #print(row)
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
    
    county_data.setdefault(state, {})
    county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})
    
    county_data[state][county]['tracts'] += 1
    county_data[state][county]['pop'] += int(pop)

# file = open('county_data.py', 'w')
# file.write(f'all_data = {pprint.pformat(county_data)}')
# file.close()
# print('DONE')