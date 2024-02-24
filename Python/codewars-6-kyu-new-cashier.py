def get_order(order):
    menu = [ 
        "Burger",
        "Fries",
        "Chicken",
        "Pizza",
        "Sandwich",
        "Onionrings",
        "Milkshake",
        "Coke"
        ]
    start_pos = 0
    res = []
    for i in range(len(order)+1):
        if order[start_pos:i+1].capitalize() in menu:
            res.append(order[start_pos:i+1].capitalize())
            start_pos = i + 1
    return ' '.join(sorted(res, key=lambda x:menu.index(x)))

print(get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"))