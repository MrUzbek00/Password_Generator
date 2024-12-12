from tkinter import *
import random
from tkinter import messagebox
import pyperclip 
PHOTO_PATH = "D:/Python/100 days Python Challenge/Intermediate/day 29/source/logo.png"
FONT_NAME = "Courier"
FILE_PATH = "D:/Python/100 days Python Challenge/Intermediate/day 29/source/My Password.txt"


#------------Logic------------#

def safe_data():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if website=="":
        website_input.config(bg="red")
    elif email== "" :
        email_input.config(bg="red")
    elif password =="":
        password_input.config(bg="red")
    else:
        is_ok = messagebox.askokcancel(title="It is importtant", message=f"Are the inserted values correct?\n {website}\n {email} \n {password}")
        if is_ok == True:
            with open(FILE_PATH, "a") as My_Password:
                My_Password.write(f"|--'{website}'--|--'{email}'--|--'{password}'--|\n")
                website_input.delete(0, END)
                email_input.delete(0, END)
                password_input.delete(0, END)
                website_input.config(bg="white")
                email_input.config(bg="white")
                password_input.config(bg="white")

def password_generator():
    generated_password = []
    global password_var
    upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    custom_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
    integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    while len(generated_password)<16:
        generated_password=[random.choice(upper_letters) for char in range(random.randint(8,10))]
        generated_password+=[random.choice(small_letters) for char in range(random.randint(2,4))]
        generated_password+=[random.choice(custom_symbols) for char in range(random.randint(2,4))]
        generated_password+=[random.choice(integers) for char in range(random.randint(2,4))]
        # generated_password.append(upper_letters[randint(0, len(upper_letters)-1)])
        # generated_password.append(small_letters[randint(0, len(small_letters)-1)])
        # generated_password.append(custom_symbols[randint(0, len(custom_symbols)-1)])
        # generated_password.append(str(integers[randint(0, len(integers)-1)]))
    # print(generated_password)
    random.shuffle(generated_password)
    my_password = ""
    for char in generated_password:
        my_password+=str(char)
    password_var.set(my_password)

def my_password_function():
    with open(FILE_PATH, "r") as my_password:
        passwords = my_password.readlines()
        password_window = Tk()
        password_window.title("Passwords")
        password_window.config(padx=50, pady=50)
        for i, line in enumerate(passwords):  # Use enumerate for row indexing
            password_label = Label(password_window, text=line.strip(), font=("Courier", 15))
            password_label.grid(column=0, row=i, sticky="w", padx=5, pady=2)  # Arrange labels in rows
       


window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200, highlightthickness=0, bd=5, relief="ridge", bg="black")
logo_image = PhotoImage(file=PHOTO_PATH)
canvas.create_image(100, 112, image=logo_image)
canvas.grid(row=0, column=1, sticky="w")

# Website Label and Entry
website_label = Label(text="Website:", font=(FONT_NAME, 15))
website_label.grid(column=0, row=1, sticky="w", padx=5, pady=5)
website = StringVar()
website_input = Entry(textvariable=website, width=53)
website_input.grid(column=1, row=1, columnspan=2, padx=5, pady=5, sticky="w")

# Email/Username Label and Entry
email_label = Label(text="Email/Username:", font=(FONT_NAME, 15))
email_label.grid(column=0, row=2, sticky="w", padx=5, pady=5)
email = StringVar()
email_input = Entry(textvariable=email, width=53)
email_input.grid(column=1, row=2, columnspan=2, padx=5, pady=5, sticky="w")

# Password Label, Entry, and Button
password_label = Label(text="Password:", font=(FONT_NAME, 15))
password_label.grid(column=0, row=3, sticky="w", padx=5, pady=5)
password_var = StringVar()
password_input = Entry(textvariable=password_var, width=31)
password_input.grid(column=1, row=3, padx=5, pady=5, sticky="w")

password_button = Button(text="Generate Password", width=14, command=password_generator)
password_button.grid(column=2, row=3, padx=5, pady=5, sticky="w")

# Add Button
add_button = Button(text="Add", width=45, command=safe_data)
add_button.grid(column=1, row=4, columnspan=2, pady=10, sticky="w")

#my_password button
my_password_button = Button(text="My Passwords", width=45, command=my_password_function)
my_password_button.grid(column=1, row=5, columnspan=2, pady=10, sticky="w")



window.mainloop()
