"""
Name: Nik Atanesian
Date: 09/01/2023
Program: Golf Scores
"""

strokes = int(input("How many strokes? "))
par = int(input("What is par? "))

par_allowed = (3, 4, 5)
if par in par_allowed:
    if par == strokes:
        print("That is a Par")
    elif par - 2 == strokes:
        print("That is an Eagle")
    elif par -1 == strokes:
        print("That is a Birdie")
    elif par + 1 == strokes:
        print("That is a Bogey")
else:
    print("That is an invalid par value.")