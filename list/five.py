"""
5.Write a Python program to count the number of strings where
 the string length is 2 or more and the first and last
 character are same from a given list of strings.
 Sample List : ['abc', 'xyz', 'aba', '1221']
"""
str=('abc','xyz', 'aba', '1221')
sum=0
for str in str:
    if len(str)>1 and str[0]==str[-1]:
        sum=sum+1
print(f"the number of string is {sum}")