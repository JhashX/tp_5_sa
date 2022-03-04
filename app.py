import requests
import json
from flask import Flask, request, jsonify, Response
server = Flask(__name__)

@server.route('/', methods=['GET'])
def start():
    return {'msg': "Software avanzado - Tarea Práctica 5 - 201800600 - Lenin Calderon"}, 200


if __name__ == '__main__':
    server.run(debug = True, host = '0.0.0.0', port = 3000)
