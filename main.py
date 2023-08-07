ADDRESSBOOK = {}

def input_error(inner):
    def wrap(*args):
        try:
            return inner(*args)
        except (IndexError, KeyError, ValueError):
            return "Invalid input. Please try again."
    return wrap

@input_error
def add_contact(data):
    name = data[0].title()
    phone = data[1]
    ADDRESSBOOK[name] = phone
    return f"Contact {name} with phone {phone} was saved"

@input_error
def change_phone(data):
    name = data[0].title()
    new_phone = data[1]
    if name in ADDRESSBOOK:
        ADDRESSBOOK[name] = new_phone
        return f"Phone number for {name} was changed"
    else:
        return f"Contact {name} not found"

@input_error
def phone_handler(data):
    name = data[0].title()
    if name in ADDRESSBOOK:
        phone = ADDRESSBOOK[name]
        return f"The phone number for {name} is {phone}"
    else:
        return f"Contact {name} not found"

@input_error
def show_all_contacts():
    if ADDRESSBOOK:
        contacts = "\n".join(f"{name}: {phone}" for name, phone in ADDRESSBOOK.items())
        return contacts
    else:
        return "No contacts found"

def exit_handler(*args):
    return "Good bye!"

def hello_handler(*args):
    return "Hello! How can I help you?"

COMMANDS = {
    add_contact: ["add"],
    change_phone: ["change"],
    phone_handler: ["phone"],
    show_all_contacts: ["show all"],
    exit_handler: ["good bye", "close", "exit"],
    hello_handler: ["hello"]
}

def command_parser(raw_str: str):
    elements = raw_str.split()
    for handler, keywords in COMMANDS.items():
        for cmd in keywords:
            if cmd.startswith(elements[0].lower()):
                if handler == show_all_contacts:
                    return handler()
                return handler(elements[1:])
    return "Unknown command"

def main():
    print("Welcome to your personal bot assistant!")
    while True:
        user_input = input("Input your command:>>> ")
        result = command_parser(user_input)
        print(result)
        if result == "Good bye!":
            break

if __name__ == "__main__":
    main()
