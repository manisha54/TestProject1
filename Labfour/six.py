"""
6.Write a Python program to count the number of even andodd numbers from a series of numbers.
"""
num=(1,2,3,4,5,6) #declaring a tuple
even=0
odd=0
for i in num:
    if not i%2:
        even=even+1
    else:
        odd=odd+1
print(f"number of even numbers is {even}")
print(f"number of odd numbers is {odd}")
