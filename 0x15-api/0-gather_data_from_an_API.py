#!/usr/bin/python3

"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    employee_id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(employee_id))
    user = user_response.json()
    params = {"userId": employee_id}
    todos_response = requests.get(url + "todos", params=params)
    todos = todos_response.json()
    completed = []

    for i in todos:
        if i.get('completed') is True:
                completed.append(i.get('title'))
    print("Employee {} is done with tasks({}/{})".format(user.get("name"),
                                                          len(completed), len(todos)))
    for j in completed:
        print("\t {}".format(j))