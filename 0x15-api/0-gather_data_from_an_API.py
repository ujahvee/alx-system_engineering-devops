#!/usr/bin/python3
"""
Returns information about his/her to list progress.
"""
import requests
from sys import argv

if __name__ == "__main__":
    todos = []
    user_id = int(argv[1])
    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users/{}".format(base_url, user_id)).json()
    req_todo = requests.get("{}todos".format(base_url),
                            params={"userId": user_id}).json()
    for todo in req_todo:
        if todo.get("userId") == user_id and todo.get("completed"):
            todos += [todo.get("title")]
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
          len(todos), len(req_todo)))
    for task in todos:
        print("\t %s" % task)
