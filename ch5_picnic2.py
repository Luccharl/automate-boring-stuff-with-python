guest_with_items = {'Alice': {'apples': 5, 'pretzels': 12},
                    'Bob': {'ham': 3, 'apples': 2}}

def total_items_brought(guest_with_items):
    
    picnic_items = {}
    
    for i in guest_with_items.values():
        for key,val in i.items():
            if key in picnic_items:
                picnic_items[key] += val
            else:
                picnic_items.setdefault(key, val)
                
    return picnic_items
        
print(total_items_brought(guest_with_items))
        