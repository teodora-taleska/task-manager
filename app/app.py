from authentication import signup, login
from tasks import filter_tasks_by, order_tasks_by, delete_task, create_task, modify_task, get_tasks
from datetime import datetime


def welcome_message():
    print("\nWelcome to Task Manager!")
    print("----------------------------")
    print("1. Login (if you already have an account)")
    print("2. Sign up (if you're a new user)")
    print("3. Exit")
    print("----------------------------")


def main():
    while True:
        welcome_message()
        welcome = input("Enter your choice (1/2/3): ")

        if welcome == "1":
            user = None
            while user is None:
                email = input("Email: ")
                password = input("Password: ")
                user = login(email, password)

            # create_task("incomplete", "work", "Test task", datetime(2023, 10, 10, 9, 43, 0), 3, 3012 )
            # get_tasks(3012)
            # modify_task(5006, "name", "hihih")

            # while True:
            #     answer = input("Do you want to continue? (yes/no) ")
            #     if answer == "no":
            #         break


        elif welcome == "2":
            name = input("Insert your name here: ")
            surname = input("Insert your surname here: ")
            email = input("Insert your email here: ")
            password = input("Insert your password here: ")
            signup(name, surname, email, password)

        elif welcome == "3":
            print("Have a great day!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
