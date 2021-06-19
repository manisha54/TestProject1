'''
2. WAP which accepts marks of four subjects and display total marks,
 percentage and grade. Hint: more than 70% –>
 distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail
'''
sub1 = float(inpu("enter your marks in first subjec: "))
sub2 = float(input("enter your marks in second subject: "))
sub3 = float(input("enter your marks in third subject: "))
sub4 = float(input("enter your marks in fouth subject: "))
total_marks = sub1 +sub2 + sub3 + sub4
print(f"the total marks of four subject is {total_marks}"
percentage = total/4
print(f'yours percentage is {percentage}')

if total_marks>70:
    grade="distinction"
elif total_marks>60%:
    grade="first division"
elif total_marks>4o:
    grade="pass"
else:
    grade:"fail"
print(f'your grade is grade')


