from flask import Flask, request

import handler


app = Flask(__name__)


@app.route("/", defaults={"path": ""}, methods=["POST", "GET"])
@app.route("/<path:path>", methods=["POST", "GET"])
def main_route(path):
    try:
        ret = handler.handle(request.get_data().decode('utf-8'))
        return ret
    except Exception as e:
        return ' '.join(e.args)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
