import logging
import sys

from flask import Flask, request
from flask.logging import default_handler

from function import handler

logging.basicConfig(
    stream=sys.stdout,
    format="%(asctime)s:%(levelname)s:%(message)s",
    level=logging.DEBUG,
)

app = Flask(__name__)
app.logger.removeHandler(default_handler)


@app.route(
    "/", defaults={"path": ""}, methods=["GET", "PUT", "POST", "PATCH", "DELETE"]
)
@app.route("/<path:path>", methods=["GET", "PUT", "POST", "PATCH", "DELETE"])
def main_route(path):
    ret = handler.handle(request.get_data(), request)
    return ret


@app.route("/_/health", methods=["GET"])
def healthcheck(path):
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
