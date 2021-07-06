'''
10. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
'''
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))
if a == b or b== c or c==a:
    print(f'the sum is zero')

elif a!=b or b!=c or c!=a:
    print(f'the sum of {a},{b} and {c} is {sum}')






