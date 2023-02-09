def separate_with_commas(given_list):
    for i in given_list:
        if len(given_list) == 1:
            print(i)
        elif i == given_list[-1]:
            print(f'and {i}')
        else:
            print(i, end=', ')


spam = ['apples','bananas', 'tofus', 'cats']
separate_with_commas(spam)