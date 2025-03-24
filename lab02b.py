"""
Name: Nik Atanesian
Date: 09/01/2023
Program: Age Classifier
"""

age = int(input("How old are you?"))

if age < 0:
    print("Error: has not been born.")
elif age <= 1:
    print("The person is an infant.")
elif age < 13:
    print("The person is a child.")
elif age < 20:
    print("The person is a teenager.")
elif age < 100:
    print("The person is an adult.")
elif age >= 100:
    print("This person is a centenarian.")