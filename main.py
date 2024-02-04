import logging

logger = logging.getLogger(__name__)


def main():
    init_logger()
    init_prompter()


def init_logger():
    logging.basicConfig(
        filename="example.log",
        filemode="w",  # overwrite log on each new execution
        format="""%(asctime)s %(levelname)-8s %(message)s \
            [%(filename)s %(funcName)s %(lineno)d]""",
        encoding="utf-8",
        level=logging.DEBUG,
    )


def init_prompter():
    # Full list of supported commands for the whole app.
    # Context-aware prompts may offer a filtered subset of these.
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

    while True:
        logging.info("Begin looping the prompter.")
        top_level_prompter(commands)


def top_level_prompter(commands):
    """Root prompter, to prompt for prompters."""
    available_commands = filter(
        lambda command: command[0] in ["dinner", "lol", "exit"], commands.items()
    )
    message = "Choose one of the prompters"
    user_input = prompt(available_commands, message)
    match user_input.lower():
        case "exit":
            logging.info("User ran command: exit (clean exit)")
            exit(0)
        case "lol":
            logging.info("User chose prompter: lol")
            prompt_for_lols(commands)
        case "dinner":
            logging.info("User chose prompter: dinner")
            prompt_for_dinner(commands)
        case _:
            logging.info("User entered miscellaneous text.")
            print("Wie bitte?")


def prompt_for_lols(commands):
    """Example prompt, to show how prompt() can be customized."""
    available_commands = filter(
        lambda command: command[0] in ["joke", "exit"], commands.items()
    )
    message = "Eggsellent choice."
    user_input = prompt(
        available_commands,
        message=message,
        prompt="Name an animal that walks backwards?",
    )
    match user_input.lower():
        case "":
            logging.info("User entered empty string.")
            pass
        case "exit":
            logging.info("User ran command: exit (clean exit)")
            exit(0)
        case "joke":
            logging.info("User ran command: joke")
            joke = "\nThere are 10 types of people in the world... \
                    \nThose who understand binary, and those who don't."
            print(joke)
        case _:
            logging.info("User entered miscellaneous text.")
            print(f"Ah yes, the mighty {user_input[::-1]}.")


def prompt_for_dinner(commands):
    """Example prompt, to show how prompt() can be customized."""
    available_commands = filter(
        lambda command: command[0] in ["monty", "exit"], commands.items()
    )
    message = "Welcome to the restaurant!"
    user_input = prompt(
        available_commands, message=message, prompt="May I take your order?"
    )
    match user_input.lower():
        case "":
            logging.info("User entered empty string.")
            pass
        case "exit":
            logging.info("User ran command: exit (clean exit)")
            exit(0)
        case "monty":
            logging.info("User ran command: monty")
            print("Monty would like the eggs and spam, please.")
        case _:
            logging.info("User entered miscellaneous text.")
            print(f"{str(user_input)}, coming right up!")


def prompt(available_commands, menu_header="Available commands", message="", prompt=""):
    """Generic prompt, to be adapted per use case."""
    if len(message) > 0:
        print(f"\n{message}")
    print(f"\n{menu_header}\n{'-'*len(menu_header)}\n")
    for cmd, desc in available_commands:
        print(f"{cmd}:\t{desc}")
    return input(f"\n{prompt}\n> ")


if __name__ == "__main__":
    main()
