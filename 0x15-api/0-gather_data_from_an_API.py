#!/usr/bin/python3
"""
Python script that leverages REST API such that given employee ID,
it returns info on the progress of TODO list.
"""

import requests
import sys

if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(sys.argv[1]))
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(sys.argv[1]))
    users_dict = users.json()
    todo_dict = todo.json()
    com_tasks = 0
    tasks = 0
    for i in todo:
        if i.get('completed') is True:
            com_tasks += 1
        else:
            tasks += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(users_dict['name'], com_tasks, tasks + com_tasks))
    for i in todo:
        if i.get('completed') is True:
            print('\t {}'.format(i.get('title')))
