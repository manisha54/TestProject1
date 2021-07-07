"""
8. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements
"""
lst=[0,1,2,3,4,5,6]
for i in lst:
    if i not in (0,4,5):
        print(i)
