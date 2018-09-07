from flask import Flask
from flask import request
from flask import jsonify


app = Flask(__name__)
app.config.from_pyfile('config.ini')

@app.route('/test/<a>/<b>/<c>/<d>/<e>', methods=['POST'])
def test(a, b, c, d, e):
    json_dict = {
        "A": a,
        "B": b,
        "C": c,
        "D": d,
        "E": e
    }
    return jsonify(json_dict)


if __name__ == '__main__':
    app.run(
        host='localhost',
    )