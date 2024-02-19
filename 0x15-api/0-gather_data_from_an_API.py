#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import json
from urllib.request import urlopen
from urllib.error import URLError

def fetch_data(url):
    try:
        with urlopen(url) as response:
            data = json.loads(response.read().decode())
        return data
    except URLError as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def fetch_employee_todo_list(employee_id):
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    todos = fetch_data(todos_url)
    user = fetch_data(user_url)

    if todos is None or user is None:
        return None

    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])

    return user['name'], completed_tasks, total_tasks, [todo['title'] for todo in todos if todo['completed']]

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = sys.argv[1]

    employee_data = fetch_employee_todo_list(employee_id)

    if employee_data:
        name, completed_tasks, total_tasks, completed_task_titles = employee_data
        print(f"Employee {name} is done with tasks ({completed_tasks}/{total_tasks}):")
        print("\n".join(["\t " + task_title for task_title in completed_task_titles]))
    else:
        print(f"No data found for employee with ID {employee_id}")
