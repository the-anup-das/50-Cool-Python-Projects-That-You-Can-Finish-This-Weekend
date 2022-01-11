import random

#user inputs
try:
    length = int(input("Enter the length of the password: "))
except ValueError:
    print("Length should be int")
    exit()
uppercase = input("include uppercase letters? Y/N - ")
special = input("include special characters? Y/N - ")
numbers = input("include numbers? Y/N - ")

#default password string
characters = list('abcdefghijklmnopqrstuvwxyz')
generated_password = ''

if uppercase == 'Y' or uppercase == 'y':
    characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
if special == 'Y' or special == 'y':
    characters.extend(list('!@#$%^&*()'))
if numbers == 'Y' or numbers == 'y':
    characters.extend(list('0123456789'))

for i in range(length):
    generated_password += random.choice(characters)

print(generated_password)