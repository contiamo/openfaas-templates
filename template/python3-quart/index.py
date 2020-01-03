import logging
import sys

from quart import Quart, request
from quart.logging import default_handler

from function import handler

logging.basicConfig(
    stream=sys.stdout,
    format="%(asctime)s:%(levelname)s:%(message)s",
    level=logging.DEBUG,
)


app = Quart(__name__)
app.logger.removeHandler(default_handler)


@app.route(
    "/", defaults={"path": ""}, methods=["GET", "PUT", "POST", "PATCH", "DELETE"]
)
@app.route("/<path:path>", methods=["GET", "PUT", "POST", "PATCH", "DELETE"])
async def main_route(path):
    payload = await request.get_data()
    ret = await handler.handle(payload, request)
    return ret


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
