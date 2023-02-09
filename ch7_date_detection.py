#! python3
# date_detection.py - Detect if given date is valid or not

import re

def detect_valid_date(date):
    
    detect_date = re.compile(r'''([0-3]\d)/  # day
                             ([0-1]\d)/      # month
                             ([1-2]\d{3})       # year 1000 to 2999
                             ''', re.VERBOSE)
    matched_date = detect_date.search(date)
    
    has_30_days = [4,6,9,11] #month with 30 days only
    
    if matched_date:
        
        day = int(matched_date.group(1))
        month = int(matched_date.group(2))
        year = int(matched_date.group(3))
        
        if day > 31 or month > 12:
            print('Invalid Date')
        
        if month == 2:  #february
            if year % 400 == 0:
                leap_year = True
            elif year % 100 == 0:
                leap_year = False
            elif year % 4 == 0:
                leap_year = True
            else:
                leap_year = False
                
            if leap_year == True:
                if day > 29:
                    print('Invalid Date')
                else:
                    print('Valid Date')
            else:
                if day > 28:
                    print('Invalid Date')
                else:
                    print('Valid Date')
        
        else:   #other months
            if month in has_30_days:
                if day > 30:
                    print('Invalid Date')
                else:
                    print('Valid Date')
            else:
                if day > 31:
                    print('Invalid Date')
                else:
                    print('Valid Date')
                
    else:
        print('No valid dates found')
        
        
detect_valid_date('23/02/2020')