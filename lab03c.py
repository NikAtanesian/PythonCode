"""
Name: Nik Atanesian
Date: 09/07/2023
Program: eCommerce Shopping
"""

tcost = 8.50
vcost = 20.00
bcost = 12.95

tshirt = int(input("How many t-shirts would you like to buy?"))
while tshirt < 0 or tshirt > 8:
    print("Invalid input.")
    tshirt = int(input("How many t-shirts would you like to buy?"))
while tshirt > 0 or tshirt < 8:    
    break

vidgame = int(input("How many video games would you like to buy?"))
while vidgame < 0 or vidgame > 2:
    print("Invalid input.")
    vidgame = int(input("How many video games would you like to buy?"))
while vidgame > 0 or vidgame < 2:    
    break

book = int(input("How many books would you like to buy?"))
while book < 0 or book > 3:
    print("Invalid input.")
    book = int(input("How many books would you like to buy?"))
while book > 0 or book < 3:    
    break

fcost = ((tshirt * tcost) + (vidgame * vcost) + (book * bcost))
print("You purchased:", tshirt, "t-shirt(s).")
print("You purchased:", vidgame, "video game(s).")
print("You purchased:", book, "book(s).")
print(f'Your total purchase is: ${fcost:,.2f} before tax.')