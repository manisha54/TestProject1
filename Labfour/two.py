"""
2.Write a Python program to convert temperatures to and from celsius, fahrenheit.C = (5/9) * (F -32)
"""
temp=float(input("enter the temperature: "))
unit=input("enter the unit of temperature(c/f)").lower()
if unit=="c":
    far=(temp*9/5)+32
    print(f'temperature in fahrenheit scale is {far}')
elif unit=='f':
    cel=(5/9)*(f-32)
    print(f'temperature in celcius is {cel}')