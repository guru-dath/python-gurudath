#Leap Year Checker
year = int(input("Which year do you want to check? "))

if year % 4 ==0 and (year % 4 != 0 or year % 4 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")

