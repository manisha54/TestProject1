'''
Q.No.9 Write a Python function that checks whether a passed string is palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward,
 e.g., madam or nurses run.
'''
def fun():
    a = input("enter a string: ")
    reverse_string=(a[::-1])
    if reverse_string==a:
        print("palindrome")
    else:
        print("not palindrome")

fun()
