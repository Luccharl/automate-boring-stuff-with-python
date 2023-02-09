import re

def format_date(date_to_format):
    #date_re = re.compile(r'[/-]')
    #matched_obj = date_re.sub('/', date)
    
    date_re = re.compile(r'''
                        ((([0-3]\d)|(\d{4})|([0-1]\d))
                        (-|/)
                        (([0-1]\d)|(\d+)|(\d{2}))
                        (-|/)
                        ((\d{4})|([0-3]\d)))
                        ''', re.VERBOSE)
    
    matched_obj = date_re.findall(date_to_format)
    
    full_date = matched_obj[0][0]
    divider = matched_obj[0][5]
    
    item1 = int(matched_obj[0][1])
    item2 = int(matched_obj[0][6])
    item3 = int(matched_obj[0][11])
    
    date_list = []
    
    date_list.append(item1)
    date_list.append(item2)
    date_list.append(item3)
    
    date_list.sort()
    
    print(date_list)
    
format_date('12/03/2003')