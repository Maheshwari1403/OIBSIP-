import tkinter as tk
from tkinter import messagebox
import string
import random
import pyperclip

# ---------------- PASSWORD GENERATOR ---------------- #
def generate_password():
    try:
        length = int(length_var.get())
    except:
        messagebox.showerror("Error", "Enter valid number!")
        return

    if length <= 0:
        messagebox.showerror("Error", "Length must be > 0")
        return

    character_set = ''
    if uppercase_var.get():
        character_set += string.ascii_uppercase
    if lowercase_var.get():
        character_set += string.ascii_lowercase
    if digits_var.get():
        character_set += string.digits
    if symbols_var.get():
        character_set += string.punctuation

    if not character_set:
        messagebox.showerror("Error", "Select at least one option")
        return

    password = ''.join(random.choice(character_set) for _ in range(length))
    password_entry.config(state="normal")
    password_entry.delete(0, 'end')
    password_entry.insert(0, password)
    password_entry.config(state="readonly")

    check_strength(password)


def copy_password():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied!")
    else:
        messagebox.showwarning("Warning", "No password!")


def toggle_password():
    if password_entry.cget('show') == "":
        password_entry.config(show="*")
        show_btn.config(text="👁 Show")
    else:
        password_entry.config(show="")
        show_btn.config(text="🙈 Hide")


def check_strength(password):
    score = 0
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1

    if len(password) >= 12:
        score += 1

    if score <= 2:
        strength_label.config(text="Weak", fg="red")
    elif score == 3:
        strength_label.config(text="Medium", fg="orange")
    else:
        strength_label.config(text="Strong", fg="green")


# ---------------- UI ---------------- #
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("450x500")
root.config(bg="#1e1e2f")

# Title
title = tk.Label(root, text="Password Generator", font=("Arial", 20, "bold"),
    bg="#1e1e2f", fg="white")
title.pack(pady=20)

frame = tk.Frame(root, bg="#2b2b3c", bd=2, relief="ridge")
frame.pack(padx=20, pady=10, fill="both", expand=True)

# Length
tk.Label(frame, text="Password Length", bg="#2b2b3c", fg="white",
   font=("Arial", 12)).pack(pady=5)

length_var = tk.StringVar()
length_entry = tk.Entry(frame, textvariable=length_var, font=("Arial", 12),
    justify="center", bd=0)
length_entry.pack(pady=5, ipadx=10, ipady=5)

# Checkboxes
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar()

for text, var in [("Uppercase", uppercase_var),
     ("Lowercase", lowercase_var),
     ("Digits", digits_var),
      ("Symbols", symbols_var)]:
    tk.Checkbutton(frame, text=text, variable=var,
      bg="#2b2b3c", fg="white",
      selectcolor="#444", font=("Arial", 10)).pack(anchor="w", padx=40)

# Generate Button
generate_btn = tk.Button(frame, text="Generate Password",
     command=generate_password,
      bg="#6C63FF", fg="white",
       font=("Arial", 12, "bold"),
        bd=0, padx=10, pady=5)
generate_btn.pack(pady=15)

# Password field
password_entry = tk.Entry(frame, font=("Arial", 14),
     justify="center", bd=0, show="*",
     state="readonly")
password_entry.pack(pady=10, ipadx=10, ipady=5)

# Show/Hide button
show_btn = tk.Button(frame, text="👁 Show", command=toggle_password,
    bg="#444", fg="white", bd=0)
show_btn.pack()

# Strength label
strength_label = tk.Label(frame, text="Strength", bg="#2b2b3c",
   font=("Arial", 11, "bold"))
strength_label.pack(pady=10)

# Copy button
copy_btn = tk.Button(frame, text="Copy Password",
    command=copy_password,
    bg="#00C897", fg="white",
    font=("Arial", 12, "bold"),
    bd=0, padx=10, pady=5)
copy_btn.pack(pady=10)

root.mainloop()