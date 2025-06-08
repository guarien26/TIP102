def get_item(items, x):
    if(len(items)< x):
        print(None)
    else:
        print(items[x])
    
items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)


items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x)