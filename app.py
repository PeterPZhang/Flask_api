from flask import Flask
from flask import request
from flask import jsonify
import json


app = Flask(__name__)
app.config.from_pyfile('config.ini')

@app.route('/test', methods=['POST'])
def test():
    #接收前端发来的数据data
    data = json.loads(request.get_data())
    A = data["a"]
    B = data["b"]
    C = data["c"]
    D = data["d"]
    E = data["e"]


    return jsonify(data)


if __name__ == '__main__':
    app.run(
        host='localhost',
    )