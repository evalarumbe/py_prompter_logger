def main():
    init_logger()
    init_prompter()


def init_logger():
    pass


def init_prompter():
    commands = {
        "dinner": "The hungry prompter",
        "lol": "The laughing prompter",
        "joke": "Tell me a classic",
        "monty": "Let Monty order",
        "exit": "Exit without saving",
    }

    # Usage examples
    # --------------
    # Different commands are available for each prompt, for context awareness.
    # Overwrite these funcs with something more useful.

    print("\nWelcome to the prompter-logger\n==============================")

    while (True):
        top_level_prompter(commands)


def top_level_prompter(commands):
    available_commands = filter(lambda command: command[0] in ["dinner", "lol", "exit"], commands.items())
    message = "Choose one of the prompters"
    user_input = prompt(available_commands, message)
    match user_input.lower():
        case "exit":
            exit(0)
        case "lol":
            prompt_for_lols(commands)
        case "dinner":
            prompt_for_dinner(commands)
        case _:
            print("Wie bitte?")


def prompt_for_lols(commands):
    available_commands = filter(lambda command: command[0] in ["joke", "exit"], commands.items())
    message = "Eggsellent choice."
    user_input = prompt(available_commands, message=message, prompt="Name an animal that walks backwards?")
    match user_input.lower():
        case "":
            pass
        case "exit":
            exit(0)
        case "joke":
            print("There are 10 types of people: those who understand binary, and those who don't.")
        case _:
            print(f"Ah yes, the mighty {user_input[::-1]}.")


def prompt_for_dinner(commands):
    available_commands = filter(lambda command: command[0] in ["monty", "exit"], commands.items())
    message = "Welcome to the restaurant!"
    user_input = prompt(available_commands, message=message, prompt="May I take your order?")
    match user_input.lower():
        case "":
            pass
        case "exit":
            exit(0)
        case "monty":
            print("Monty would like the eggs and spam, please.")
        case _:
            print(f"{str(user_input)}, coming right up!")


def prompt(available_commands, menu_header="Available commands", message="", prompt="Well?"):
    if len(message) > 0:
        print(f"\n{message}")
    print(f"\n{menu_header}\n{'-'*len(menu_header)}\n")
    for cmd, desc in available_commands:
        print(f"{cmd}:\t{desc}")

    return input(f"\n{prompt}\n> ")

if __name__ == "__main__":
    main()
