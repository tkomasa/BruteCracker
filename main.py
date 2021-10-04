from random import randint
from time import time

# taking input from user
user_pass = input("Enter your password: ")
t0 = time()
# storing alphabet letter to use them to crack password
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
alphnum = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z',
           '1', '2', '3', '4', '5', '6', '7', '8', '9']

# initializing an empty string
guess = ""
iterations = 0

if user_pass.isalpha():
    while guess != user_pass:
        guess = ""
        for letter in range(len(user_pass)):
            guess_letter = alphabet[randint(0, 25)]
            guess = str(guess_letter) + str(guess)
        print(guess)
        iterations += 1
if user_pass.isnumeric():
    while guess != user_pass:
        guess = ""
        for letter in range(len(user_pass)):
            guess_letter = numbers[randint(0, 8)]
            guess = str(guess_letter) + str(guess)
        print(guess)
        iterations += 1
else:
    if user_pass.isalnum():
        while guess != user_pass:
            guess = ""
            for letter in range(len(user_pass)):
                guess_letter = alphnum[randint(0, 34)]
                guess = str(guess_letter) + str(guess)
            print(guess)
            iterations += 1

t1 = time()
print("Your password is:", guess)
t_total = t1 - t0
t_total = round(t_total, 3)
print("Time elapsed:", t_total)
print("Iterations:", iterations)
