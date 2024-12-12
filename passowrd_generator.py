#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []
password_list=[random.choice(letters) for char in range(nr_letters)]
# for char in range(nr_letters):
#   password_list.append(random.choice(letters))
password_list+=[random.choice(symbols) for char in range(nr_symbols)]
# for char in range(nr_symbols):
#   password_list += random.choice(symbols)
password_list+=[random.choice(numbers) for char in range(nr_numbers)]
# for char in range(nr_numbers):
#   password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password} {len(password)}")




generated_password = []
global password_var
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
custom_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# while len(generated_password)<16:
generated_password=[random.choice(upper_letters) for char in range(random.randint(8,10))]
generated_password+=[random.choice(small_letters) for char in range(random.randint(2,4))]
generated_password+=[random.choice(custom_symbols) for char in range(random.randint(2,4))]
generated_password+=[random.choice(integers) for char in range(random.randint(2,4))]
    # generated_password.append(upper_letters[random.randint(0, len(upper_letters)-1)])
    # generated_password.append(small_letters[random.randint(0, len(small_letters)-1)])
    # generated_password.append(custom_symbols[random.randint(0, len(custom_symbols)-1)])
    # generated_password.append(str(integers[random.randint(0, len(integers)-1)]))
random.shuffle(generated_password)
print(type(generated_password))
my_password = ""
for char in generated_password:
    my_password+=str(char)

print(f" My pasowrd: {my_password} {len(my_password)}")
#password_var.set("".join(generated_password[0:16]))



