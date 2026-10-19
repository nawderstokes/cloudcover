import os

import redis
from flask import Flask, jsonify

from cloudcover import cloud_cover

app = Flask(__name__)
r = redis.Redis(host=os.environ.get("REDIS_HOST", "localhost"), 
                port=6379, 
                decode_responses=True,
)

@app.get("/")
def index():
    cached = r.get("cloud_cover")
    if cached is not None:
        return jsonify({"cloud_cover": float(cached), "cached": True})
    value = cloud_cover()
    r.setex("cloud_cover", 600, value)
    return jsonify({"cloud_cover": value, "cached": False})