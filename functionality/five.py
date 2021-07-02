'''
Q.No.5 Write a function calledshow_stars(rows).Ifrowsis 5, it should print thefollowing:***************
'''

def show_stars(rows):
    for i in range(1,rows+1):
        print('*' * i)
num=int(input('enter the number of rows: '))
show_stars(num)

