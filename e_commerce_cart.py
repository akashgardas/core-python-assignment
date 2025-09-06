def calc_price(cart: dict) -> float:
    '''
    Calculates the total price of items in the cart
    Arguments: cart - type: dictionary
    Return: Total Price of items in the cart
    '''
    # Handling if cart is empty
    if len(cart) == 0:
        return 0
    
    total_price = 0
    for cost in cart.values():
        total_price += cost
    
    # Discount
    if len(cart) > 5:
        total_price -= 0.1 * total_price
    
    return total_price

cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
cart_items2 = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500, 'Mouse Pad': 300, 'Laptop Stand': 2500}

# Discount not applicable
print(f'Total price of your purchase is {calc_price(cart_items)}')

# Discount applicable
print(f'Total price of your purchase is {calc_price(cart_items2)}')