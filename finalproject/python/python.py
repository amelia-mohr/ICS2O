from flask import Flask
from flask import request
import logging

logging.basicConfig(filename='record.log', level=logging.DEBUG)

app = Flask(_name_)

@app.route('/',methods=['POST'])
def order():
    request_data = request.get_json()
    app.logger.warning(request_data)
    return 'HELLOOOOOOOOOOOOOO!!!!!'