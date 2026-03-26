from collections import namedtuple
contact = namedtuple("contact",["name","phone","email"])

def get_user_prompt(prompt):
    while True:
        value = (input(prompt)).strip()
        if value:
            return value
        continue

def get_contact():
    name = get_user_prompt("Enter a name to get contact: ").title()
    return name
    

def search_contact(name,contact_list):
    for person in contact_list:
        if name == person.name:
            return person
    return None
    
def formatting_contact(name,contact):
    if contact is None:
        print(f"{name} is not in contact list.")
    else: 
        print(f"Name: {contact.name} | Phone: {contact.phone} | Email: {contact.email}")    

def main():
    contact_list = [contact("Ishan","7066157341","ishank@gmail.com"), contact("Gen","9765334881","gencha123@gmail.com"), contact("Shin","8233549904","shindayo97@gmail.com")]
    name_store = get_contact()
    contact_store = search_contact(name_store,contact_list)
    formatting_contact(name_store,contact_store)

if __name__ == "__main__":
    main()

