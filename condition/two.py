'''
3. If temperature is greater than 30, it's a hot day other wise if it's less than 10;
 it's a cold day; otherwise, it's neither hot nor cold.
'''
temp = int(input("enter the temperature: "))
if temp>30:
    print("it is hot day")
elif temp<10:
    print("it is cold day")
else:
    print("it is neither hot nor cold")
