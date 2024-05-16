from flask import Flask, jsonify, request
from pro_data import data

app = Flask(__name__)
@app.route("/")
def index():
    return jsonify({
        'data':data,
        'message':'success'
    })
@app.route('/planet')
def planet():
    name = request.args.get('name')
    planet_data = next(item for item in data if item['name']==name)
    return jsonify({
        'data':planet_data,
        'message':'success'
    })

app.run(debug=True)
