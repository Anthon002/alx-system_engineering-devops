#!/usr/bin/python3
"""this script will exports a to do list info for an  employee ID to CSV format."""
import csv
import requests as req
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    usr = req.get(url + "users/{}".format(user_id)).json()
    username = usr.get("username")
    todos = req.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, i.get("completed"), i.get("title")]
         ) for i in todos]