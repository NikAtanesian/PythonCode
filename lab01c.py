"""
Name: Nik Atanesian
Date: 08/22/2023
Program: Shopping Calculator
"""

price1 = float(input('The price of the first item is:'))
quantity1 = float(input('The number of items is:'))
total1 = float(price1 * quantity1)
tax1 = float(total1 * 0.07)
price2 = float(input('The price of the second item is:'))
quantity2 = float(input('The number of items is:'))
total2 = float(price2 * quantity2)
tax2 = float(total2 * 0.07)
price3 = float(input('The price of the third item is:'))
quantity3 = float(input('The number of items is:'))
total3 = float(price3 * quantity3)
tax3 = float(total3 * 0.07)
final = float((total1) + (total2) + (total3))
total_tax = float(tax1 + tax2 + tax3)
print('The total price for the first item is $', format(total1, ',.2f'))
print('The total price for the first item is $', format(total2, ',.2f'))
print('The total price for the first item is $', format(total3, ',.2f'))
print('The total price (without tax) is $', format(final, ',.2f'))
print('The amount of tax is $', format(total_tax, ',.2f'))
print('The final price is $', format(final + total_tax, ',.2f'))