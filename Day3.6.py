#True Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combine = name1 + name2
p1 = combine.lower()

t = p1.count("t")
r = p1.count("r")
u = p1.count("u")
e = p1.count("e")

true = t+r+u+e

l = p1.count("l")
o = p1.count("o")
v = p1.count("v")
e = p1.count("e")

love = l+o+v+e

Truelove = int(str(true) + str(love))
 

if (Truelove < 10) or (Truelove > 90) :
    print(f"Your score is {Truelove}, you are alright together.")
    
elif (Truelove >= 40) and (Truelove <= 50):
    print(f"Your score is {Truelove}, you go together like coke and mentos.")
else:
    print(f"Your score is {Truelove}")