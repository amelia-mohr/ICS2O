from flask import Flask
from flask import request
app = Flask(_name_)

@app.route('/',methods=['POST'])
def order():
    request_data = request.get_json()
    print(request_data)

