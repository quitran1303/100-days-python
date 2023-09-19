print("Welcome to Love Calculator")
name1 = input("Please input name for person 1: \n")
name2 = input("Please input name for person 2: \n")

your_names = (name1 + name2).lower()
#TRUE LOVE

true_values = your_names.count('t') + your_names.count('r') + your_names.count('u') + your_names.count('e')
love_values = your_names.count('l') + your_names.count('o') + your_names.count('v') + your_names.count('e')

score = int(true_values*10 + love_values)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")