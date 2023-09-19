print("Welcome to pizza order")

print(
    "The price for pizza is $15 for S, $20 for M, and $25 for L"\
    "Add pepperoni for S/M +$2, for L +$3" \
    "Add extra chese +$1"
)

size = input("Please choose your type: S, M, or L? ")
add_peperoni = input("Do you want to add pepperoni into your pizze? Y or N: ")
extra_chesse = input("Do you want to add extra chesse? Y or N: ")

print(f"You choose pizza size: {size} with {'Yes' if (add_peperoni=='Y') else 'No'} pepperoni and \
       {'Yes' if (extra_chesse == 'Y') else 'No'} cheese")
price = 0
if size == 'S':
    price = 15
    if add_peperoni == 'Y':
        price += 2
    if extra_chesse == 'Y': 
        price += 1
elif size == 'M':
    price = 20
    if add_peperoni == 'Y':
        price += 2
    if extra_chesse == 'Y': 
        price += 1
else: 
    price = 25
    if add_peperoni == 'Y':
        price += 2
    if extra_chesse == 'Y': 
        price += 1


print(f"You choose pizza size: {size} with {'Yes' if (add_peperoni=='Y') else 'No'} pepperoni\
    and {'Yes' if (extra_chesse == 'Y') else 'No'} cheese with price: {price}")