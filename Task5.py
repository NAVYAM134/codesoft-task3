import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self, root):
        self.contacts = []
        self.root = root
        self.root.title("Contact Book")
        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Contact Book", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=4, pady=10)

        # Add Contact Section
        tk.Label(self.root, text="Name:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Phone:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Email:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Address:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=5, column=0, columnspan=2, pady=10)

        # Display Contacts
        tk.Button(self.root, text="View Contacts", command=self.view_contacts).grid(row=6, column=0, columnspan=2, pady=10)

        # Search Section
        tk.Label(self.root, text="Search by Name/Phone:").grid(row=7, column=0, padx=5, pady=5, sticky="e")
        self.search_entry = tk.Entry(self.root)
        self.search_entry.grid(row=7, column=1, padx=5, pady=5)

        tk.Button(self.root, text="Search", command=self.search_contact).grid(row=8, column=0, columnspan=2, pady=10)

        # Contact List Display
        self.result_text = tk.Text(self.root, width=50, height=10)
        self.result_text.grid(row=9, column=0, columnspan=4, pady=10)

        # Update and Delete
        tk.Button(self.root, text="Update Contact", command=self.update_contact).grid(row=10, column=0, columnspan=2, pady=5)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=11, column=0, columnspan=2, pady=5)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if name and phone:
            self.contacts.append(Contact(name, phone, email, address))
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and Phone are required fields.")

    def view_contacts(self):
        self.result_text.delete(1.0, tk.END)
        if not self.contacts:
            self.result_text.insert(tk.END, "No contacts available.\n")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                self.result_text.insert(tk.END, f"{i}. {contact}\n")

    def search_contact(self):
        query = self.search_entry.get().strip()
        self.result_text.delete(1.0, tk.END)
        results = [contact for contact in self.contacts if query in (contact.name, contact.phone_number)]
        if results:
            for contact in results:
                self.result_text.insert(tk.END, f"{contact}\n")
        else:
            self.result_text.insert(tk.END, "No contact found.\n")

    def update_contact(self):
        query = self.search_entry.get().strip()
        for contact in self.contacts:
            if contact.name == query:
                new_phone = self.phone_entry.get().strip()
                new_email = self.email_entry.get().strip()
                new_address = self.address_entry.get().strip()

                if new_phone:
                    contact.phone_number = new_phone
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address

                messagebox.showinfo("Success", "Contact updated successfully!")
                self.clear_entries()
                return

        messagebox.showerror("Error", "Contact not found.")

    def delete_contact(self):
        query = self.search_entry.get().strip()
        initial_count = len(self.contacts)
        self.contacts = [contact for contact in self.contacts if contact.name != query]
        if len(self.contacts) < initial_count:
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Contact not found.")
        self.clear_entries()

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)

# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
