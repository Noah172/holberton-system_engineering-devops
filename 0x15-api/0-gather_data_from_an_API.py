#!/usr/bin/python3
"""
script that given employee ID,
returns information about his/her TODO list progress.
"""

if __name__ == '__main__':

    import json
    import requests
    import sys

    EMPLOYEE = ""
    NUMBER_TASKS = 0
    TOTAL_TASKS = 0
    TASK_TITLE = []

    employee = requests.get('https://jsonplaceholder.typicode.com/users')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = todos.json()
    employees = employee.json()
    for tas in tasks:
        if tas.get("userId") == eval(sys.argv[1]):
            if tas.get("completed") == 1:
                NUMBER_TASKS += 1
                TASK_TITLE.append(tas.get("title"))
            TOTAL_TASKS += 1
    for emplo in employees:
        if emplo.get('id') == eval(sys.argv[1]):
            EMPLOYEE = emplo.get('name')
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE,
                                                          NUMBER_TASKS,
                                                          TOTAL_TASKS))
    for task in TASK_TITLE:
        print("\t {}".format(task))
