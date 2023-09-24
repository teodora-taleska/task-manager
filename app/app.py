from authentication import signup, login
from tasks import filter_tasks_by, order_tasks_by, delete_task, create_task, modify_task, get_tasks, export_tasks_to_csv
from datetime import datetime


def welcome_message():
    print("\nWelcome to Task Manager!")
    print("----------------------------")
    print("1. Login (if you already have an account)")
    print("2. Sign up (if you're a new user)")
    print("3. Exit")
    print("----------------------------")


def is_number(input_str):
    try:
        float(input_str)  # Try to convert the input to a float
        return True  # If successful, it's a number
    except ValueError:
        return False  # If ValueError is raised, it's not a number


def export_tasks(tasks, userId, name):
    q = input("Would you like to export the tasks to a CSV file? (yes/no): ").strip().lower()

    if q == "yes":
        export_tasks_to_csv(tasks, f"{userId}_{name}.csv")
    elif q == "no":
        pass
    else:
        print("Invalid response. Please enter 'yes' or 'no'")


def choice_one():
    user = None
    while user is None:
        email = input("Email: ")
        password = input("Password: ")
        user = login(email, password)
    userId = user["uid"]

    while True:
        print("\nTask Manager Menu:")
        print("1. View Tasks")
        print("2. Create Task")
        print("3. Filter Tasks By")
        print("4. Order Tasks By")
        print("5. Modify Task")
        print("6. Delete Task")
        print("7. Log Out")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            tasks = get_tasks(userId)
            for t in tasks:
                print(t)
            export_tasks(tasks, userId, "tasks")
            input("To go back, please press any key: ")

        elif choice == "2":
            print("How many tasks do you want to create? ")
            n = input("Enter a number: ")

            if is_number(n):
                for i in range(int(n)):
                    name = input("Name: ").lower()

                    while True:
                        category = input("Category (work/school/personal/shopping/event): ").lower()
                        if category not in ["work", "school", "personal", "shopping", "event"]:
                            print("Invalid parameter")
                        else:
                            break

                    while True:
                        status = input("Status (complete/incomplete): ").lower()
                        if status not in ["complete", "incomplete"]:
                            print("Invalid parameter")
                        else:
                            break

                    while True:
                        priority = input("Priority (1/2/3) (3=lowest): ").lower()
                        if priority not in ["1", "2", "3"]:
                            print("Invalid parameter")
                        else:
                            break

                    print("Deadline (enter numbers) ")
                    day = input("Day: ")
                    month = input("Month: ")
                    year = input("Year:")
                    hour = input("Hour: ")
                    minutes = input("Minutes: ")
                    seconds = input("Seconds: ")

                    create_task(status,
                                category,
                                name, datetime(int(year), int(month), int(day), int(hour), int(minutes), int(seconds)),
                                priority,
                                userId)
                input("To go back, please press any key: ")

        elif choice == "3":
            print("By which parameter would you like to filter the tasks?")
            filter_param = input("Filter parameter: ").lower()
            filter_value = input("Filter value: ").lower()
            tasks = filter_tasks_by(userId, filter_param, filter_value)
            for t in tasks:
                print("\n", t, "\n")
            export_tasks(tasks, userId, f"filtered_by_{filter_param}")
            input("To go back, please press any key: ")

        elif choice == "4":
            print("By which parameter would you like to order the tasks?")
            order_param = input("Order parameter: ").lower()
            way = input("Ordering way (asc/desc): ").lower()
            while True:
                if way not in ["asc", "desc"]:
                    print("Invalid parameter.")
                elif way == "asc":
                    asc = True
                    break
                elif way == "desc":
                    asc = False
                    break
            tasks = order_tasks_by(userId, order_param, asc)
            for t in tasks:
                print(t)
            export_tasks(tasks, userId, f"ordered_by_{order_param}")
            input("To go back, please press any key: ")

        elif choice == "5":
            n = input("How many tasks do you want to modify? ")
            for i in range(int(n)):
                tid = input("Which task do you want to modify? (enter task id): ")
                modify_param = input("Which parameter do you want to modify? ").lower()
                modification = input("Enter your modification: ").lower()
                modify_task(userId, tid, modify_param, modification)
            input("Modifications completed. To go back, please press any key: ")

        elif choice == "6":
            n = input("How many tasks do you want to delete? ")
            for i in range(int(n)):
                tid = input("Which task do you want to delete? (enter task id): ")
                delete_task(userId, tid)
            input("Deletion process completed. To go back, please press any key: ")

        elif choice == "7":
            break
        else:
            print("\nInvalid choice. Please enter a valid option (1-6).")


def choice_two():
    name = input("Insert your name here: ")
    surname = input("Insert your surname here: ")
    email = input("Insert your email here: ")
    password = input("Insert your password here: ")
    signup(name, surname, email, password)


def main():
    while True:
        welcome_message()
        welcome = input("Enter your choice (1/2/3): ")

        if welcome == "1":
            choice_one()
        elif welcome == "2":
            choice_two()
        elif welcome == "3":
            print("Have a great day!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
