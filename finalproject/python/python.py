from flask import Flask
from flask import request
import logging

logging.basicConfig(filename='record.log', level=logging.DEBUG)

app = Flask(__name__)

@app.route('/',methods=['POST'])
def order():
    request_data = request.get_json()
    app.logger.warning(request_data)
    with open("orders.txt", "a") as file:
        file.write(request_data)
    return 'HELLOOOOOOOOOOOOOO!!!!!'