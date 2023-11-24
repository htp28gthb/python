"""Module providing function to help a customer order a cup of coffee"""
import sys

# change this to your coffee shop name
COFFEE_SHOP_NAME = "HTP28"

print("Hello, welcome to " + COFFEE_SHOP_NAME +" Coffee!!!\n")

# ask for the customer name
name = input("What's your name?\n")

if name == "Ben":
    evil_status = input("Are you evil?\n")
    if evil_status == "Yes":
        print("\nYou're not welcome here Evil Ben!! Get out!!\n")
        sys.exit(0)
    else:
        print("Oh, so you're on of those good Bens, Come on in!!")
else:
    print("\nHello " + name + ", thank you so much for coming in today.\n")

MENU = ["Black Coffee", "Espresso", "Latte", "Cappuccino", "Frappuccino"]

print(name + ", Here is the menu")
print(MENU)

while True:
    # ask for what the customer's order
    order = input("\nWhat would you like?\n")

    if order in MENU:
        if order == "Black Coffee":
            PRICE = 3
        elif order == "Espresso":
            PRICE = 8
        elif order == "Latte":
            PRICE = 9
        elif order == "Cappuccino":
            PRICE = 12
        elif order == "Frappuccino":
            PRICE = 13

        break
    else:
        print("\nSorry, we don't sell that. Please choose from the menu.")

# ask for the quantity the customer wants to order
quantity = input("\nHow many coffees would you like?\n")

total = PRICE * int(quantity)

print("\nThe total price is: $" + str(total))

print("\nSounds good " + name + ", we'll serve your " + quantity + " " + order + " in a moment.")
