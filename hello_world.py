import os
os.system('cls||clear') # this line clears the screen 'cls' = windows 'clear' = unix
# below is my main script
print("hello world!")
print("Das klappt ja bislang ganz gut :-)")
x = float(input("What's x? "))
y = float(input("What's y? "))
# z = round(x / y, 2)
z = x / y

print(f"{z:.2f}")
 