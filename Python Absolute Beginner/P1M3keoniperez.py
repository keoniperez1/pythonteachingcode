def cheeseStore():
    print("Welcome to Cheese Store Online!")
    customer_nm=input('Please provide your full name:')
    chzMax=print('We have 100 pounds of Cheddar cheese')
    chzMin=print('The Minimum you can order is 0.5 pound.')
    priceCz=print('$8 per pound.')
    pricepp= 8
    order_amount=input('How much would you like?')
    if float(order_amount) >= 100.0:
        print("Sorry, we don't have enough for your order")
    elif float(order_amount)<= 0.5:
        print('Sorry, we cannot sell you for less than 0.5 pounds.')
    else:
        print(customer_nm.title(), 'your order would of',order_amount, 'pounds at $8. The total would be: $', int(order_amount) * pricepp)

cheeseStore()