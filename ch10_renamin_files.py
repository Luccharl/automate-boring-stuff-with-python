import os,re,shutil

date_pattern = re.compile(r'''^(.*?)
                           (([0|1])?\d)-
                           ((0|1|2|3)?\d)-
                           ((19|20)\d\d)
                           (.*?)$
                       ''', re.VERBOSE)

for american_format_name in os.listdir('.'):
    
    #search for files that matched the reg_ex given
    obj_matched = date_pattern.search(american_format_name)
    
    #skip files with no dates
    if obj_matched == None:
        continue
    
    before_date = obj_matched.group(1)
    month_part = obj_matched.group(2)
    day_part = obj_matched.group(4)
    year_part = obj_matched.group(6)
    after_date = obj_matched.group(8)
    
    #european style filename
    euro_format_name = f'{before_date}{day_part}-{month_part}-{year_part}{after_date}'
    
    #getting the absolute paths
    abs_working_dir = os.path.abspath('.')
    american_format_name = os.path.join(abs_working_dir, american_format_name)
    euro_format_name = os.path.join(abs_working_dir, euro_format_name)
    
    #renamin the files
    shutil.move(american_format_name, euro_format_name)