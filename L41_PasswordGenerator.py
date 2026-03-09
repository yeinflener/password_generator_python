import random

letters = ['a', 'b', 'c', 'd', 'e', 'f','g','h','i','j','k','l','A', 'B', 'C', 'D','E','F','G','H', 'I', 'J','K']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','*','(',')']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy level

password = ""
# nr_letters = 4
for char in range(0,nr_letters):
    password = password + random.choice(letters)
    # random_character = random.choice(letters)
    # password = password + random_character

for char in range(0,nr_symbols):
    password = password + random.choice(symbols)
    # random_symbol = random.choice(symbols)
    # password = password + random_symbol

for char in range(0,nr_numbers):
    password = password + random.choice(numbers)
    # random_number = random.choice(numbers)
    # password = password + random_number
print(password)






