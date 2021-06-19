1.#function=no parameter and no statement
def add(a,b):
    a = int(input("enter the first value: "))
    b = int(input("enter the second value: "))
    c=a+b


    print(f'the sum of {a} and {b} is {c}')

2.#sub=parameter and no return statement
def sub(a,b):
    c=a-b
    print(f"the sub of {a} and {b} is {c}")
3.#mul= no parameter and return statement
def product():
    a=int(input("enter the first value: "))
    b=int(input("enter the second value: "))
    c=a*b
    return c
4.div=parameter and return statement
def div(a,b):
    c=a/b
    return c