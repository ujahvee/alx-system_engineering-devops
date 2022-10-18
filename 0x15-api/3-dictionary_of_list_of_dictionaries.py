#!/usr/bin/python3

"""
export all to-do list progress data in the JSON format.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get("{}users".format(base_url)).json()
    with open("todo_all_employees.json", mode="w") as json_file:
        task_dct = {}
        for user in users:
            user_id = user.get("id")
            username = user.get("username")
            req_tasks = requests.get("{}todos".format(
                base_url), params={"userId": user_id}).json()
            task_dct[user_id] = []
            for tasks in req_tasks:
                task_dct[user_id] += [{"username": username,
                                       "task": tasks["title"],
                                       "completed": tasks["completed"]}]
        data = json.dumps(task_dct)
        json_file.write(data)
