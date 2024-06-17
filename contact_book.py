import os

class ContactManager:
    def __init__(self):
        self.contacts = {}
        self.filename = "contacts.txt"
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    phone, name, email, address = line.strip().split('|')
                    self.contacts[phone] = {
                        'name': name,
                        'email': email,
                        'address': address
                    }

    def save_contacts(self):
        with open(self.filename, "w") as file:
            for phone, details in self.contacts.items():
                line = f"{phone}|{details['name']}|{details['email']}|{details['address']}\n"
                file.write(line)

    def input_contact_details(self, existing_phone=None):
        name = input("Enter name: ").strip()
        while not name:
            print("Name cannot be empty. Please enter a valid name.")
            name = input("Enter name: ").strip()

        if existing_phone:
            phone = existing_phone
        else:
            phone = input("Enter phone number: ").strip()
            while not phone or phone in self.contacts:
                if not phone:
                    print("Phone number cannot be empty. Please enter a valid phone number.")
                else:
                    print("Phone number already exists. Please enter a different phone number.")
                phone = input("Enter phone number: ").strip()

        email = input("Enter email: ").strip()
        address = input("Enter address: ").strip()

        return phone, name, email, address

    def add_contact(self):
        print("Adding a new contact...")
        phone, name, email, address = self.input_contact_details()
        self.contacts[phone] = {
            'name': name,
            'email': email,
            'address': address
        }
        print(f"Contact for {name} added successfully.")
        self.save_contacts()

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available!")
            return
        print("\nContact List:")
        for phone, details in self.contacts.items():
            print(f"Name: {details['name']}, Phone: {phone}, Email: {details['email']}, Address: {details['address']}")

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ").strip()
        found_contacts = []
        for phone, details in self.contacts.items():
            if search_term.lower() in (phone.lower(), details['name'].lower()):
                found_contacts.append((phone, details))
        if found_contacts:
            print("\nFound Contacts:")
            for phone, details in found_contacts:
                print(f"Name: {details['name']}, Phone: {phone}, Email: {details['email']}, Address: {details['address']}")
        else:
            print("Contact not found.")

    def update_contact(self):
        phone = input("Enter the phone number of the contact to update: ").strip()
        if phone in self.contacts:
            print("Updating contact....")
            phone, name, email, address = self.input_contact_details(existing_phone=phone)
            self.contacts[phone] = {
                'name': name,
                'email': email,
                'address': address
            }
            print("Contact updated successfully!")
            self.save_contacts()
        else:
            print("Contact not found!")

    def delete_contact(self):
        phone = input("Enter the phone number of the contact to delete: ").strip()
        if phone in self.contacts:
            del self.contacts[phone]
            print("Contact deleted successfully....")
            self.save_contacts()
        else:
            print("Contact not found.")

    def display_menu(self):
        while True:
            print("\nContact Manager")
            print("1. Add Contact\t\t2. View Contact List")
            print("3. Search Contact\t4. Update Contact")
            print("5. Delete Contact\t6. Exit")
            choice = input("\nChoose an option: ").strip()
            
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting Contact Manager.....")
                break
            else:
                print("Invalid choice! please try again.")

if __name__== "__main__":
    manager = ContactManager()
    manager.display_menu()