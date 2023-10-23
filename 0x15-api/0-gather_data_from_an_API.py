#!/usr/bin/python3
"""This script will returns a to-do list information from an api of a given employee ID."""
import sys
import requests as req


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    usr = req.get(url + "users/{}".format(sys.argv[1])).json()
    todos = req.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [i.get("title") for i in todos if i.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        usr.get("name"), len(completed), len(todos)))
    [print("\t {}".format(j)) for j in completed]
