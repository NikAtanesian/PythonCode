"""
Name: Nik Atanesian
Date: 08/29/2023
Program: Rectangle comparison
"""

width1 = input("What is the width of your first rectangle?")
height1 = input("What is the height of your first rectangle?")

rect1 = int(int(width1) * int(height1))

width2 = input("What is the width of your second rectangle?")
height2 = input("What is the height of your second rectangle?")

rect2 = int(int(width2) * int(height2))

if rect1 > rect2:
    print("Rectangle 1 wins!")
elif rect2 > rect1:
    print("Rectangle 2 wins!")
else:
    print("They are equal")