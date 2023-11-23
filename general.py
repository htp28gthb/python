# Say hello with the name that user inputs
name = input("What's your name? ")
print("Hello, " + name)


# Allow the user to input 2 numbers, then compare and sum them
x = int(input("Number of a: "))
y = int(input("Number of b: "))
z = x + y
if x < y:
    print (f"x > y, and the result is {z}")
elif x > y:
    print (f"x < y, and the result is {z}")
else:
    print(f"x = y, and the result is {z}")


# Count to 8 and print message
i = 0
size = 10
while i < size:
    i += 1
    print(f"{i} ", end="")
    if i == 8:
        print("Number " + str(i) + " is found.")
        break
    else:
        continue


for j in range(3):
    print("#" * 3)