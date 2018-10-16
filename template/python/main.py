from flask import Flask, request

from handler import handler


app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    print(request)
    data = request.get_data()
    return handler(data)


app.run(host='0.0.0.0', port=8080)
