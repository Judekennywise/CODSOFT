import tkinter as tk
from tkinter import Label, Entry, Button, messagebox, font
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")

        # Increase the text size by setting a larger font
        large_font = font.Font(size=14)

        self.label = Label(master, text="Enter the desired length of the password:", font=large_font)
        self.label.pack(pady=10)

        

        self.entry = Entry(master, font=large_font)
        self.entry.pack(pady=10)

        self.generate_button = Button(master, text="Generate Password", command=self.generate_password, font=large_font)
        self.generate_button.pack(pady=10)
        
        self.generated_label = Label(master, text="", font=large_font)
        self.generated_label.pack(pady=10)
    def generate_password(self):
        try:
            length = int(self.entry.get())
            password = self._generate_password(length)
            self.generated_label.config(text=f"Generated Password: '{password}'")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number for password length.")

    def _generate_password(self, length):
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        digits = string.digits
        special_characters = string.punctuation

        all_characters = lowercase_letters + uppercase_letters + digits + special_characters

        if length < 1:
            return "Invalid password length. Please enter a positive number."

        password = ''.join(random.choice(all_characters) for _ in range(length))
        return password

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
