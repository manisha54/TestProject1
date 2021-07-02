'''
Q.No.2 Write a function calledfizz_buzzthat takes a number.If the number is divisible by 3,
it should return “Fizz”.If it is divisible by 5, it should return “Buzz”.
If it is divisible by both 3 and 5, it should return “FizzBuzz”.Otherwise,
 it should return the same number.
'''
def fizz_buzz(b):
    if b/3==b//3:
        return "fizz_buzz"
    elif b/5==b//5:
        return "buzz"
    elif b/3==b//3 and b/5==b//5:
        return "fizzbuzz"
b=float(input("enter a number: "))
fizz_buzz(b)
print(fizz_buzz(b))