"""
Name: Nik Atanesian
Date: 09/07/2023
Program: Rewrite For Loop as a While Loop -- While
"""

age = input("How old are you? ")

age = int(age)
number = 0

print("Happy Birthday To You ! ")

while number < age:
    print(f"Are you {number+1}")
    number += 1