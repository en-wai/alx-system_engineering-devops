#!/usr/bin/python3
"""Python cript to export data in the CSV format"""
import csv
import requests as r
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    employee = r.get(url + "users/{}".format(employee_id)).json()
    username = employee.get("username")
    todo = r.get(url + "todos", params={"userId": employee_id}).json()

    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([employee_id, username, elm.get("completed"),
                          elm.get("title")]) for elm in todo]
