'''
1. Check whether 5 is in list of first 5 natural numbers or not. Hint: List => [1,2,3,4,5]
'''
list=[1,2,3,4,5]
given_number=5
if given_number in range(1,6):
    print(f'number is in the list')
else:
    print(f'number is not in the list')