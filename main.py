import factory
from console_interface import print_menu, confirm_operation, client_do_another_operation

if __name__ == "__main__":

    client = factory.Client(input("\n Type your CPF:"))

    while client.is_online:
        
        client.commit_to_db()
        print_menu()
        option = int(input("\n Enter your choice: "))

        if option == 1:
            value = input("\n How much do you want to deposit? ")
            confirmation = confirm_operation(operation="deposit", value=value)
            if confirmation == "y":
                client.deposit(value)
            client.is_online = client_do_another_operation()

        if option == 2:
            value = input("\n How much do you want to withdraw? ")
            confirmation = confirm_operation(operation="withdraw", value=value)
            if confirmation == "y":
                client.withdraw(value)
            client.is_online = client_do_another_operation()

        if option == 3:
            client.extract_and_balance()
            client.is_online = client_do_another_operation()

        if option == 4:
            break

    client.commit_to_db()
    print("\n Thank you for using our service.")
