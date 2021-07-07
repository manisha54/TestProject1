"""
3.Write a Python program to guess a number between 1 to 9.
Note :User is prompted to enter a guess. If the user guesses wrong then the
prompt appears again until the guess is correct, on successful guess,
 user will get a "Well guessed!" message, and the program will exit.
"""
"""
import random
guess_num=int(input("enter a number between 1 to 9: "))
random_num= random.randint(1,9)
while random_num!=guess_num:
    guess_num=int(input("enter a number between 1 to 9 until the guess is correct: "))
print("well guessed")
"""
import random
guess_num=int(input("enter a number between 1 to 9: "))
random_num = random.randint(1,9)
while random_num!= guess_num:
    if guess_num>random_num:
        print("guess_number is too high!")
        guess_num = int(input("enter a number between 1 to 9: "))
    elif guess_num<random_num:
        print("guess_num is too low")
        guess_num = int(input("enter a number between 1 to 9: "))
print("your guess is correct")

