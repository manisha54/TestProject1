'''
4. Given three integers, print the smallest one. (Three integers should be user input)
'''
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
c=int(input("enter the third number: "))
if a<b and a<c :
    print(f"{a} is the smallest")
elif b<a and b<c :
    print(f"{b} is the smallest")
else:
    print(f"{c} is the smallest")