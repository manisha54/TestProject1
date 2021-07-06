'''
Q.No.1 Write a Python function to find the Max of three numbers
'''
def max():
    a = int(input("enter the number : "))
    b = int(input("enter the number: "))
    c = int(input("enter the number: "))
    if a > b and a > c:
        print(f"{a}is the max")
    elif b > a and b > c:
        print(f"{b}is the max")
    elif c > a and c > b:
        print(f"{c}is the max")
max()

