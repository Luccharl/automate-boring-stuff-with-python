import pyinputplus as pyip
import time

def sandwich_maker():
    
    item_prices = []

    #PRICES OF EACH SANDWICH COMPONENTS
    bread_type = {'Wheat': 2.00, 'White': 1.85, 'Sourdough': 1.30}
    protein_type = {'chicken': 2.55, 'turkey': 2.75, 'ham': 2.30, 'tofu': 1.50}
    cheese_type = {'cheddar': 0.50 , 'swiss': .65, 'mozarella': 0.75}
    mayo = 0.50
    mustard = 0.50
    lettuce = 1.30
    tomato = 1.20
    
    print('Let\'s make a sandwich!')
    time.sleep(1)

    bread_prompt = 'What type of bread do you want? \n'
    bread_choice = pyip.inputMenu(['Wheat', 'White', 'Sourdough'], bread_prompt, lettered=True)
    print()

    if bread_choice in bread_type:
        bread_cost = bread_type[bread_choice]
        item_prices.append(bread_cost)

    protein_prompt = 'Choose your protein: \n'
    protein_choice = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], protein_prompt , lettered=True)
    print()

    if protein_choice in protein_type:
        protein_cost = protein_type[protein_choice]
        item_prices.append(protein_cost)

    want_cheese = pyip.inputYesNo('Do you want cheese? (Y/N): ')
    print()
    
    if want_cheese == 'yes':
        
        cheese_prompt = 'What type of cheese do you want? \n'
        cheese_choice = pyip.inputMenu(['cheddar', 'swiss', 'mozarella'], cheese_prompt, lettered=True)
        print()
        
        if cheese_choice in cheese_type:
            cheese_cost = cheese_type[cheese_choice]
            item_prices.append(cheese_cost)

    want_mayo = pyip.inputYesNo('Do you want mayo? (Y/N): ')
    if want_mayo == 'yes':
        item_prices.append(mayo)
    want_mustard = pyip.inputYesNo('Do you want mustard? (Y/N): ')
    if want_mustard == 'yes':
        item_prices.append(mustard)
    want_lettuce = pyip.inputYesNo('Do you want lettuce? (Y/N): ')
    if want_lettuce == 'yes':
        item_prices.append(lettuce)
    want_tomato = pyip.inputYesNo('Do you want tomato? (Y/N): ')
    if want_tomato == 'yes':
        item_prices.append(tomato)

    return item_prices

def total_cost():
    
    total_per_sandwich = 0
    
    cost = sandwich_maker()
    
    for item in range(len(cost)):
        total_per_sandwich += cost[item]     
        
    print()
    sandwich_count = pyip.inputInt('How many sandwiches do you want? ', default=1)
    total_cost = total_per_sandwich * sandwich_count
    
    print(f'The total cost is ${total_cost}')
    
total_cost()
    

