def calculate_total_cost(cart):
    total_cost = 0
    for item in cart:
        total_cost = total_cost + (item['price'] * item['quantity'])

    return total_cost


cart = [
    {'name' : 'Apple', 'price' : 40, 'quantity' : 5},
    {'name' : 'Banana', 'price' : 30, 'quantity' : 12},
    {'name' : 'Orange', 'price' : 60, 'quantity' : 8}
]

print(calculate_total_cost(cart))