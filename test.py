import json
import requests


def log(s):
    print()
    print(s)
    print()


with open("config.json", "r") as f:
    config = json.load(f)

with open(config["index"], "r") as f:
    index = f.read()

url = "http://localhost:5000"


# -- GET / --

log("GET /")

with open(config["index"], "r") as f:
    index = f.read()

log(index)

r = requests.get(url)

log(r)


# -- GET /data --

log("GET /data")

with open(config["data"], "r") as f:
    data = json.load(f)

log(data)

r = requests.get(url + "/data")

log(r)


# -- POST /data --

log("POST /data")

data = { "foo": "bar" }

r = requests.post(url + "/data", json=data)

log(r)

