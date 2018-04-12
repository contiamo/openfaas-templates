#!/usr/bin/env python

from handler import handler
from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    print(request)
    data = request.get_data()
    return handler(data)

app.run(host='0.0.0.0', port=8080)
