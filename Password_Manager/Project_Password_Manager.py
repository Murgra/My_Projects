from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# Window

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Picture

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file=r"Projects\Password_Manager\logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Password Save

def clear(*args):
    for n in args:
        n.delete(0, "end")

def save(new_data):
    try:
        with open(r"Projects\Password_Manager\data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
            with open(r"Projects\Password_Manager\data.json", "w") as file:
                json.dump(new_data, file, indent=4)
    else:
        data.update(new_data)

        with open(r"Projects\Password_Manager\data.json", "w") as file:
            json.dump(data, file, indent=4)


def add_info():
    website = website_entry.get()
    mail = mail_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
        "email": mail,
        "password": password,
    }
}

    if website == "" or  password == "":
        messagebox.showinfo(title="Empty fields", message="Please don't leave any fields empty!")

    else:
        save(new_data)
        clear(website_entry, password_entry)


# Password Check
        
def search():
    website = website_entry.get()
    with open(r"Projects\Password_Manager\data.json", "r") as file:
        data = json.load(file)
    try: 
        web = data[website]
    except KeyError:
        messagebox.showinfo(title="No data", message="No data for this website.")
    else:
        messagebox.showinfo(title=f"{website}", message=f"Mail: {web['email']}\nPassword: {web['password']}")

# Password Generator

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]

    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]


    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# Text

website_text = Label(text="Website:")
website_text.grid(column=0, row=1)

mail_text = Label(text="Email/Username:")
mail_text.grid(column=0, row=2)

password_text = Label(text="Password:")
password_text.grid(column=0, row=3)

# Entry

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()


mail_entry = Entry(width=35)
mail_entry.grid(column=1, row=2, columnspan=2)
mail_entry.insert(0, "user@gmail.com")


password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add_info)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1)

window.mainloop()