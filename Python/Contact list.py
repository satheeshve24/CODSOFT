contacts = {}

def add_contact(name, phone_number, email, address):
    contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}
    print("Contact added successfully.")


def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone_number']}, Email: {details['email']}, Address: {details['address']}")

def search_contact(query):
    found = False
    for name, details in contacts.items():
        if query in name or query == details['phone_number']:
            print(f"Name: {name}, Phone: {details['phone_number']}, Email: {details['email']}, Address: {details['address']}")
            found = True
    if not found:
        print("Contact not found.")


def update_contact(name, phone_number, email, address):
    if name in contacts:
        contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


print("Welcome to Contact Management System")

while True:
    print("\nMenu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        add_contact(name, phone_number, email, address)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        query = input("Enter name or phone number to search: ")
        search_contact(query)
    elif choice == "4":
        name = input("Enter name of contact to update: ")
        phone_number = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        update_contact(name, phone_number, email, address)
    elif choice == "5":
        name = input("Enter name of contact to delete: ")
        delete_contact(name)
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")


