#!flaskblog.py

from flask import Flask, render_template, request, url_for, redirect
from ffactor import Data

data = Data()
app = Flask(__name__)

@app.route("/")
@app.route("/moody")
def index():
    return render_template('index.html', data = data)

@app.route("/inputs" , methods=['POST'])
def inputs():
    data1 = request.form['data1']
    data2 = request.form['data2']
    data.read_ed(data1)
    data.read_Re(data2)
    data.calculate_f()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug = True) 