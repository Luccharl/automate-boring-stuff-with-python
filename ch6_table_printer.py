table_data = [['apples', 'oranges', 'cherries', 'banana'],
         ['Alice','Luc','Marc', 'Arman'],
         ['dog', 'cat', 'rabbit', 'owl']]

def print_table(table):

    col_width = [0] * len(table)
    
    count = 0
    while count < len(table):
        for item in table[count]:
            if len(item) > col_width[count]:
                col_width[count] = len(item)
        count += 1
    
    for word in range(len(table[0])):
        for item in range(len(table)):
            print(table[item][word].rjust(col_width[item]), end=' ')
        print()
              
print_table(table_data)