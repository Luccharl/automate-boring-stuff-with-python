player_inventory = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def total_game_inventory(inventory):
    
    total_items = 0
    
    print('Inventory contents: ')
    
    for key, val in inventory.items():
        print(f'{val} {key}')
        total_items += int(val)
    
    print(f'Total number of items: {total_items}')
        
def add_to_inventory(inventory, new_loot):
    
    for item in new_loot:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.setdefault(item, 1)
    
    return inventory

updated_inv = add_to_inventory(player_inventory,dragon_loot)       
total_game_inventory(updated_inv)