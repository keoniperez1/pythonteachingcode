# [ ] create, call and test fishstore() function 
def fishstore(fish, price):
    fish=fish.capitalize()
    price=price.capitalize()
    return fish + ' ' + price

fish_entry=input('Fish in stock: Salmon, Snapper, Tilapia. Choosing:')
price_entry=input('Please provide the price for the type of fish chose:')
fish3= fishstore(fish_entry, price_entry)

print('Report for Keoni Perez. Fish type:',fish_entry,'costs $'+price_entry)





def fishtype():
    fish_entry= input('Fish in stock: Salmon, Snapper, Tilapia. Choosing:')
    return fish_entry.capitalize()

def fishpr():
    price_entry=input('Please provide the price for the type of fish chose:')
    return price_entry

print('Report for Keoni Perez. Fish type:',fishtype(),'costs $'+fishpr())