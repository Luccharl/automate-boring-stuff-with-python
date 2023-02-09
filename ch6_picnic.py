from turtle import right


def disp_picnic(picnic_items, left_width, right_width):
    print('PICNIC ITEMS'.center(left_width + right_width, '-'))
    for key,value in picnic_items.items():
        print(f'{key.ljust(left_width, ".") + str(value).rjust(right_width)}')
        
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
disp_picnic(picnicItems, 12, 5)
disp_picnic(picnicItems, 20, 6)