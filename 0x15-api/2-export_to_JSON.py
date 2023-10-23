#!/usr/bin/python3
"""this script will export  to do list info for a given employee ID to JSON format."""
import json
import requests as req
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    usr = req.get(url + "users/{}".format(user_id)).json()
    username = usr.get("username")
    todos = req.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": username
            } for i in todos]}, jsonfile)
