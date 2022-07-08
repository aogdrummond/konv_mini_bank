menu_options = {
    1: "Deposit",
    2: "Withdraw",
    3: "Extract and Balance",
    4: "Exit",
}


def print_menu():
    """
    Prints the main menu in the console
    """
    for key in menu_options.keys():
        print(key, "--", menu_options[key])


def confirm_operation(operation: str, value: int) -> bool:
    """
    Asks the client to confirm the operation requested
    """
    try:
        value = int(value)
        answer = input(
            f"\n Are you sure you want to {operation} {value} reais?[y/n] "
        ).lower()
        return answer

    except:
        print("\n The value must be a positive integer.")
        pass


def client_do_another_operation() -> bool:
    """
    Asks to the client whether he/she wants to do
    another operation or end the ap
    """
    while True:
        answer = input("\n Do you want to do another operation?[y/n] ").lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("\n The answer must be whether 'y'[yes] or 'n'[no].")
