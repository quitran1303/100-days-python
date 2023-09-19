print('''
 .d88b.  .d88b. 88888b.d88b. .d8888b  
d88P"88bd8P  Y8b888 "888 "88b88K      
888  88888888888888  888  888"Y8888b. 
Y88b 888Y8b.    888  888  888     X88 
 "Y88888 "Y8888 888  888  888 88888P' 
     888                              
Y8b d88P                              
 "Y88P"
''')

print("Welcome to the Treasure Island \n You will win if you find the gem \n")

left = input("Left or right? L or R ?")
wait = input("Swim or wait? S or W? ")
door = input("Which door do you choose? Red, Blue, Yellow?")

if left == 'R':
    print('game over!!!')
else:
    if wait == 'S':
        print('game over!!!')
    else:
        if door == "Yellow":
            print("You are winner!!!")
        else:
            print ('game over!!!')


