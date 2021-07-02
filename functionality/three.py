'''
Q.No.3 Write a function calledshowNumbersthat takes a parameter calledlimit.
It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
 For example, if the limit is 3, it should print:0 EVEN,1 ODD,2 EVEN
'''
def shownumber(limit):
    for i in range(0,3):
        if i%2==0:
            print(f'{i}: even')
        else:
            print(f"{i}: odd")
num=int(input("enter a number: "))
shownumber(num)
