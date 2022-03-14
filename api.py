from flask import Flask, request

import main

app = Flask(__name__)

@app.route('/find', methods=['GET', 'POST'])
def find():
    input_path = 'test/image.png'
    if request.method == 'POST':
        static_file = request.files['file']
        static_file.save(input_path)
        capacity = request.form['capacity']
        spots = int(capacity) - main.model(input_path)
        return str(spots)