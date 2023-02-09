guest_with_items = {'Alice': {'apples': 5, 'pretzels': 12},
                    'Bob': {'ham': 3, 'apples': 2}}

def total_items_brought(guest_with_items,items):
    total_brought = 0
    for i in guest_with_items.values():
        total_brought += i.get(items, 0)
        
    return total_brought

print(f"APPLES - {total_items_brought(guest_with_items, 'apples')}")