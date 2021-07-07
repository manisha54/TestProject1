"""
9.Write a program to find the factorial of a number.
"""
num=int(input("enter a number: "))
product=1
for i in range(2,num+1):
    product=product*i
print(f"the factorial number is {product}")
