#!/usr/bin/python3

"""
export data in the JSON format information about
his/her to-do list progress.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    user_id = int(argv[1])
    base_url = "https://jsonplaceholder.typicode.com/"
    username = requests.get(
        "{}users/{}".format(base_url, user_id)).json().get("username")
    req_tasks = requests.get("{}todos".format(base_url), params={
                             "userId": user_id}).json()
    with open("{}.json".format(user_id), mode="w") as json_file:
        task_dct = {user_id: []}
        for tasks in req_tasks:
            task_dct[user_id] += [{"task": tasks["title"],
                                   "completed": tasks["completed"],
                                   "username": username}]
        data = json.dumps(task_dct)
        json_file.write(data)
