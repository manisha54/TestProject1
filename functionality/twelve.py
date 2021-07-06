'''
Write a python program to check whether the number is Armstrong number or not using function:
[Hint: 153 - 1*1*1 + 5*5*5 + 3*3*3]
'''
def armstrong(num):
    sum=0
    a=num
    for i in range(1,num):
        digit=a%10
        sum=sum + digit**3
        a//=10
    if num==sum:
        print(f"{num}is armstrong")
    else:
        print(f'{num} is not armstrong')
num = int(input("enter a number: "))
armstrong(num)
