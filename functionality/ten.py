'''
10. Write a program to find the factorial of a number using functions.
'''
def factorial(num):
    product=1
    for i in range(2,num+1):
        product=product*i
    return product
num=int(input("enter a number: "))
print(factorial(num))
