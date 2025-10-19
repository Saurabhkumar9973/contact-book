# Contact Management System

contacts = {}

def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    contacts[phone] = {"name": name, "email": email, "address": address}
    print("Contact added successfully!\n")


def view_contacts():
    if not contacts:
        print("No contacts found!\n")
        return
    print("\n--- Contact List ---")
    for phone, details in contacts.items():
        print(f"Name: {details['name']} | Phone: {phone}")
    print()


def search_contact():
    choice = input("Search by Name or Phone? (n/p): ").lower()
    found = False

    if choice == 'n':
        name = input("Enter Name to Search: ").strip().lower()
        for phone, details in contacts.items():
            if details['name'].lower() == name:
                print(f"\nFound: {details['name']} | Phone: {phone} | Email: {details['email']} | Address: {details['address']}\n")
                found = True
                break
    elif choice == 'p':
        phone = input("Enter Phone Number to Search: ").strip()
        if phone in contacts:
            details = contacts[phone]
            print(f"\nFound: {details['name']} | Phone: {phone} | Email: {details['email']} | Address: {details['address']}\n")
            found = True

    if not found:
        print("Contact not found!\n")


def update_contact():
    phone = input("Enter Phone Number of contact to update: ").strip()
    if phone in contacts:
        print("Leave blank if you don’t want to change a field.")
        name = input("Enter New Name: ").strip()
        email = input("Enter New Email: ").strip()
        address = input("Enter New Address: ").strip()

        if name:
            contacts[phone]["name"] = name
        if email:
            contacts[phone]["email"] = email
        if address:
            contacts[phone]["address"] = address

        print("Contact updated successfully!\n")
    else:
        print("Contact not found!\n")


def delete_contact():
    phone = input("Enter Phone Number of contact to delete: ").strip()
    if phone in contacts:
        del contacts[phone]
        print("Contact deleted successfully!\n")
    else:
        print("Contact not found!\n")


def menu():
    while True:
        print("===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")


# Run Program
menu()
