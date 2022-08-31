import tkinter
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_text = password_entry.get()
    password_entry.delete(0, len(password_text))
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_to_file():
    web_name = website_entry.get()
    email_name = email_entry.get()
    password = password_entry.get()
    sms = f"These are your details Website: {web_name}, Email: {email_name}, Password: {password}"
    is_ok = messagebox.askokcancel(title=web_name, message=sms)
    if len(web_name) == 0 or len(email_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Info", message="DON'T LEAVE THE FIELDS EMPTY.")
    else:
        if is_ok:
            with open("password_data.txt", "a") as details:
                details.write("\n")

                details.write(f"{web_name.upper()} | {email_name} | {password}")
                website_entry.delete(0, len(web_name))
                password_entry.delete(0, len(password))


# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("PASSWORD GENERATOR")
window.geometry("900x600")
window.config(bg="#123456")
window.resizable(False, False)
window.config(pady=20, padx=20)


canvas = tkinter.Canvas(width=550, height=350, highlightthickness=0, bg="#123456")
img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(275, 175, image=img)
canvas.grid(column=1, row=0)
font_style = ("Arial", 15, "bold")
email = "jobby123@gmail.com"

website_label = tkinter.Label(window, text="Website", font=("Arial", 18, "bold"), bg="#123456", fg="white")
website_label.grid(column=0, row=1)

email_label = tkinter.Label(window, text="Email", font=("Arial", 18, "bold"), bg="#123456", fg="white")
email_label.grid(column=0, row=2)

password_label = tkinter.Label(window, text="Password", font=("Arial", 18, "bold"), bg="#123456", fg="white")
password_label.grid(column=0, row=3)

# Entries
website_entry = tkinter.Entry(width=40)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = tkinter.Entry(width=40)
email_entry.grid(column=1, row=2)
email_entry.insert(0, email)


password_entry = tkinter.Entry(width=40)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = tkinter.Button(text="Generate Password", font=font_style, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", font=font_style, width=10, command=save_to_file)
add_button.grid(column=2, row=4)

window.mainloop()
