'''
4.Input the weight of a person in either kg or lbs. If the person provides his/her
weight in kg then convert it into lbs
else convert it to kg.
'''
weight=int(input("enter your weight: "))
unit = input('enter unit (kg/lbs): ').lower()
if unit =='kg':
    converted_weight = weight*2.20462
    print(f"your weight is {converted_weight} lbs")
elif unit == 'lbs':
    converted_weight = weight*0.453592
    print(f'your weight is {converted_weight} kg')
else:
    print("use either 'kg' or 'lbs' as unit.")