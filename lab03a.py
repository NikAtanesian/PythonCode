"""
Name: Nik Atanesian
Date: 09/07/2023
Program: Bug Collector Problem
"""

bugs = 0
total = 0

for day in range(5):
    bugs = int(input("Enter the number of bugs collected today."))
    total += bugs

print("Total bugs collected: ", total)