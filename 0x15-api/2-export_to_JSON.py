#!/usr/bin/python3
"""Python Script to export to-do list information to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(employee_id)).json()
    user_name = employee.get("username")
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump({employee_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": user_name
            } for t in todos]}, jsonfile)
