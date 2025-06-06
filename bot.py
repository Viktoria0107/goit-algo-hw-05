def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command" 
        except KeyError:
            return "Invalid argument entered for command"
        except IndexError:
            return "Enter the name after command"
     

    return inner


def parse_input(user_input):
    if len(user_input) == 0:
        return " "
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args



@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Change contact"

@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]

def all_contact(contacts):
    return contacts

   
def main():
    contacts = {}

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command == " ":
            print("Not command")

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(all_contact(contacts))
       
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()