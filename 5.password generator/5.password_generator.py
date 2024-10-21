import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password=[]

password.append(random.sample(letters, nr_letters))



password.append(random.sample(symbols,nr_symbols))



password.append(random.sample(numbers, nr_numbers))



final_password = []

for i in password[0]:
    final_password.append(i)

for i in password[1]:
    final_password.append(i)

for i in password[2]:
    final_password.append(i)




random.shuffle(final_password)



user_password=("")

for letter in final_password:
    user_password+=letter

print(f"your password is {user_password}")
