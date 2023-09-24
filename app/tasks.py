import csv

from models import Tasks, Session
from sqlalchemy import desc, asc, and_

session = Session()


def create_task(status, category, name, deadline, priority, userId):
    task = Tasks(status, category, name, deadline, priority, userId)
    session.add(task)
    session.commit()
    print("The task has been successfully created.")


def get_tasks(uid):
    result = session.query(Tasks).filter_by(userId=uid).limit(10)
    return result


def order_tasks_by(uid, order_param, ascending=True):
    # Define a dictionary to map user-friendly filter parameters to actual columns
    column_map = {
        'priority': Tasks.priority,
        'status': Tasks.status,
        'name': Tasks.name,
        'deadline': Tasks.deadline,
        'category': Tasks.category
    }

    # Check if the filter_param is valid and get the corresponding column
    if order_param in column_map:
        column = column_map[order_param]
    else:
        raise ValueError("Invalid parameter")

    # Create a query using the selected column
    query = session.query(Tasks).filter_by(userId=uid).order_by(asc(column) if ascending else desc(column)).limit(10)

    return query


def modify_task(uid, tid, modify_param, modification):
    task = session.query(Tasks).filter_by(tid=tid).first()

    if task and uid == task.userId:
        setattr(task, modify_param, modification)
        session.commit()
        print(f"The {modify_param} of the task has been successfully modified.")
    else:
        print("Task not found.")


def filter_tasks_by(uid, filter_param, f):
    column_map = {
        'priority': Tasks.priority,
        'status': Tasks.status,
        'name': Tasks.name,
        'deadline': Tasks.deadline,
        'category': Tasks.category
    }

    if filter_param not in column_map:
        raise ValueError("Invalid filter parameter!")

    column = column_map[filter_param]

    if filter_param == "name":
        tasks = session.query(Tasks).filter(and_(Tasks.userId == uid, column.ilike(f"%{f}%"))).limit(10)
    else:
        tasks = session.query(Tasks).filter(and_(Tasks.userId == uid, column == f)).limit(10)

    return tasks


def delete_task(uid, tid):
    task = session.query(Tasks).filter_by(tid=tid).first()

    if task and uid == task.userId:
        session.delete(task)
        session.commit()
        print("Task has been successfully deleted!")
        return True
    else:
        print("The task does not exist in your scope. Please try again.")
        return False


def export_tasks_to_csv(tasks, file_path):
    # Define the fieldnames for the CSV file (column names)
    fieldnames = ['tid', 'status', 'category', 'name', 'date', 'deadline', 'priority', 'userId']

    # Open the CSV file for writing
    with open(file_path, 'w', newline='') as csvfile:
        # Create a CSV writer object
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header (field names) to the CSV file
        writer.writeheader()

        # Write each task as a row in the CSV file
        for task in tasks:
            writer.writerow({
                'tid': task.tid,
                'status': task.status,
                'category': task.category,
                'name': task.name,
                'date': task.date,
                'deadline': task.deadline,
                'priority': task.priority,
                'userId': task.userId
            })

