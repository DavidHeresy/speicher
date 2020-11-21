import json
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


# -- CONFIG --

with open("config.json", "r") as f:
    config = json.load(f)


# -- APP --

app = FastAPI()


# -- INDEX --

assert "index" in config.keys(), "config.json must contain key 'index'"
with open(config["index"], "r") as f:
    index = f.read()

@app.get("/", response_class=HTMLResponse)
async def get_index():
    return index


# -- DATA --

assert "data" in config.keys(), "config.json must contain key 'data'"
data_path = config["data"]

@app.get("/data")
async def get_data():
    with open(data_path, "r") as f:
        data = json.load(f)
    return data

@app.post("/data")
async def post_data(data: dict):
    with open(data_path, "w") as f:
        json.dump(data, f)
    return data
