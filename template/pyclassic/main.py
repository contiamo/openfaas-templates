#!/usr/bin/env python
from contextlib import redirect_stdout
import io
import os

from flask import Flask, request

from handler import handler

app = Flask(__name__)

def touch(fname, mode=0o666, dir_fd=None, **kwargs):
    flags = os.O_CREAT | os.O_APPEND
    with os.fdopen(os.open(fname, flags=flags, mode=mode, dir_fd=dir_fd)) as f:
        os.utime(f.fileno() if os.utime in os.supports_fd else fname,
            dir_fd=None if os.supports_fd else dir_fd, **kwargs)

@app.route('/', methods=['GET', 'POST'])
def main():
    print(request)

    data = request.get_data()
    f = io.StringIO()
    with redirect_stdout(f):
        handler(request.get_data())
    return f.getvalue()

# mark the container as healthy
touch("/tmp/.lock")
# start the server
app.run(host='0.0.0.0', port=8080)
