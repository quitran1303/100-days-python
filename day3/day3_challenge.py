year = int(input("Please input a year:"))

div4 = year % 4
div100 = year % 100
div400 = year % 400

if div4 == 0:
    if div100 == 0:
        if div400 == 0:
            print(f"{year} is a leaf year")
        else:
            print(f"{year} is not leaf year")
    else:
        print(f"{year} is a leaf year")
else:
    print(f"{year} is not a leaf year")