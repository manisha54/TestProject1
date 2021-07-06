'''
6. A person’s body mass index (BMI) is defined as:
BMI=mass in kg / (height in m)2.
'''
mass = float(input("enter the mass of a body(in kg): "))
height = float(input("enter the height of a body(in metre): "))
BMI = mass / (height) ** 2
print(f" the body mass index of person is {BMI} ")