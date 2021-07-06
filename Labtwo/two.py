'''
2. WAP which accepts marks of four subjects and display total marks,
 percentage and grade. Hint: more than 70% –>
 distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail
'''
sub1 = float(input("enter your marks in first subject: "))
sub2 = float(input("enter your marks in second subject: "))
sub3 = float(input("enter your marks in third subject: "))
sub4 = float(input("enter your marks in fourth subjec: "))
total_marked= sub1 +sub2 + sub3 + sub4/
print(f"the total marks  is {total_marked}"
percentage=total_marked/400*100
print(f'your percentage is {percentage}')
if percentage>70:
    grade="distinction"
elif percentage>60:
    grade="first division"
elif percentage>4o:
    grade="pass"
else:
    grade="fail"
print(f'your grade is grade')


