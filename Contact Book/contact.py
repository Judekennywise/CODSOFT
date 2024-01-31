import tkinter as tk
from tkinter import simpledialog, messagebox

class ContactManager:
    def __init__(self, master):
        self.master = master
        master.title("Contact Manager")

        self.contacts = {}

        # Labels and Entry widgets for contact information
        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.phone_label = tk.Label(master, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.address_label = tk.Label(master, text="Address:")
        self.address_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.address_entry = tk.Entry(master)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Buttons for actions
        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(master, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=5)

        self.search_button = tk.Button(master, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=5)

        self.update_button = tk.Button(master, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=7, column=0, columnspan=2, pady=5)

        self.delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            messagebox.showinfo("Success", f"Contact '{name}' added successfully.")
        else:
            messagebox.showerror("Error", "Name and Phone are required.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Contacts", "No contacts found.")
        else:
            contact_list = "\n".join([f"{name}: {details['Phone']}" for name, details in self.contacts.items()])
            messagebox.showinfo("Contacts", contact_list)

    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter name or phone number:")
        if search_term:
            matches = [f"{name}: {details['Phone']}" for name, details in self.contacts.items()
                       if search_term.lower() in name.lower() or search_term in details['Phone']]
            if matches:
                messagebox.showinfo("Search Results", "\n".join(matches))
            else:
                messagebox.showinfo("Search Results", "No matches found.")

    def update_contact(self):
        name = simpledialog.askstring("Update", "Enter the name of the contact to update:")
        if name in self.contacts:
            new_phone = simpledialog.askstring("Update", f"Enter new phone number for {name}:")
            if new_phone:
                self.contacts[name]["Phone"] = new_phone
                messagebox.showinfo("Success", f"Phone number for {name} updated successfully.")
            else:
                messagebox.showerror("Error", "Invalid phone number.")
        else:
            messagebox.showerror("Error", f"Contact '{name}' not found.")

    def delete_contact(self):
        name = simpledialog.askstring("Delete", "Enter the name of the contact to delete:")
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", f"Contact '{name}' deleted successfully.")
        else:
            messagebox.showerror("Error", f"Contact '{name}' not found.")

def main():
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
