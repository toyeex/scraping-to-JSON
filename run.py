import requests
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/idrates')
def id_rates():
    source = requests.get('http://www.floatrates.com/daily/idr.json')
    json_data = source.json()
    return render_template('index2.html',data = json_data.values())


if __name__ == '__main__':
    app.run(debug=True)