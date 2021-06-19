'''
4.Input the weight of a person in either kg or lbs. If the person provides his/her
weight in kg then convert it into lbs
else convert it to kg.
'''
weight=int(input("enter your weight: "))
unit = input('Is the weight of a person in kg or lbs?: ')
kg=int(weight*2.2)
lbs=int(weight/2.2)
if unit==kg:
    print(f"the weight in kilogram is: {lbs}")
elif unit==lbs:
    print(f'the weight in pound is: {kg}')
else:
    print("please provide the valid weight")