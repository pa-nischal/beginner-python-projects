#This is a simple contact phonebook program.

contacts = ["1234567890"]
names = ["Nischal"]


n = int(input("Enter the number of contacts you want to store:"))
for i in range(n):
    new_name = input("Enter the contact name:")
    new_contact = input("Enter the contact number")
    names.append(new_name)
    contacts.append(new_contact)
    print(f"New contact {new_name} - {new_contact} added to the phonebook!")

print(f"You have {len(contacts)} contacts stored in your phonebook!")

display = input("Do you want to display your phonebook?(y/n)")
if display.upper() == "Y":
    for i in range(len(contacts)):
        print(f"{names[i]} - {contacts[i]}")

input("Press any key to exit!")