from flask import Flask, request, jsonify

app = Flask(__name__)

cart = []

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    item = request.get_json()
    cart.append(item)
    return jsonify(cart)

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    item = request.get_json()
    cart.remove(item)
    return jsonify(cart)

@app.route('/view_cart', methods=['GET'])
def view_cart():
    return jsonify(cart)