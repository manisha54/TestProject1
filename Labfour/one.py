"""
1.Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
between 1500 and 2700 (both included).
"""
lower=int(input("enter the lower range: "))
upper=int(input("enter the upper range: "))
for i in range(lower,upper+1):
    if i%7==0 and i%5==0:
            print(i,end=' ')