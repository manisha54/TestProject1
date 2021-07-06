'''
Q.No.7 Write a Python function that accepts a string and
calculate the number of upper case letters and lower case letters.
'''
def upperandlowercase(sentence):
    upper=0
    lower=0
    for i in sentence:
        if i>='A' and i<='Z':
            upper=upper+1
        elif i>='a'and i<='z':
            lower=lower+1
    print(f'upper case:{upper}')
    print(f'lower case:{lower}')
a=str(input("enter something: "))
print(upperandlowercase(a))

