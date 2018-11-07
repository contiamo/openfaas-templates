from flask import Flask, request

import handler


app = Flask(__name__)


@app.route("/", defaults={"path": ""}, methods=["POST", "GET"])
@app.route("/<path:path>", methods=["POST", "GET"])
def main_route(path):
    ret = handler.handle(request.get_data().decode('utf-8'))
    return ret


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
