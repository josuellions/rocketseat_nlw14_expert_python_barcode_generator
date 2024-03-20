from flask import Flask, request, jsonify


app = Flask(__name__)

def create_tag():
    body = request.json
    product_code = body.get('product_code')



