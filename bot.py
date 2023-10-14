def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(contacts, name, phone):
    if name in contacts:
        return f"Contact '{name}' already exists."
    contacts[name] = phone
    return "Contact added."


def change_contact(contacts, name, phone):
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Contact '{name}' not found."


def show_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        return f"Contact '{name}' not found."


def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) != 2:
                print("Invalid command. Please use 'add [name] [phone]'")
            else:
                name, phone = args
                print(add_contact(contacts, name, phone))
        elif command == "change":
            if len(args) != 2:
                print("Invalid command. Please use 'change [name] [phone]'")
            else:
                name, phone = args
                print(change_contact(contacts, name, phone))
        elif command == "phone":
            if len(args) != 1:
                print("Invalid command. Please use 'phone [name]'")
            else:
                name = args[0]
                print(show_phone(contacts, name))
        elif command == "all":
            print(show_all(contacts))
        else:
            print(
                "Invalid command. Available commands: hello, add, change, phone, all, close, exit"
            )


if __name__ == "__main__":
    main()
