'''
Q.No.4 Write a function that returns the sum of multiples of 3 and 5 between 0 andlimit(parameter).
 For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20
'''

def sum_of_mul(limit):
    sum=0
    for i in range(i,limit+1):
        if i%3==0 or i%5==0:
            sum=sum+i
     print(sum)
a=int(input("enter a limit: "))
print(sum_of_numbers(limit))

