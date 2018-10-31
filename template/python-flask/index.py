from flask import Flask, request

from handler import handle


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    data = request.get_data().decode('utf-8')
    return handle(data)


app.run(host='0.0.0.0', port=5000, debug=True)
