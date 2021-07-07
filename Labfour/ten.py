"""
10.Write a Python program that accepts a string and calculate the number of digits and letters
"""
str = input("enter a string: ")
digit=0
letter=0
for i in str:
    if i.isdigit():
        digit=digit+1
    elif i.isalpha():
        letter=letter+1
    else:
        pass
print(f"the total number of digit is {digit}")
print(f"the total number of letter is {letter}")