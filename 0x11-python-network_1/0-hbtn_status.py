#!/usr/bin/python3
"""
    This script fetches from https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import urllib.request as ur
    url = 'https://alx-intranet.hbtn.io/status'
    with ur.urlopen(url) as response:
        content = response.read()
        print("Body resonse:")
        print("\t- type:",type(content))
        print("\t- content:{}".format(content))
        print("\t- utf8 content:",content.decode('utf-8'))
