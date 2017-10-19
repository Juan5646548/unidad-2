from kepler import ley_kepler
from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def home() -> '302':
    return redirect('/entry')


@app.route('/entry')
def go_entry() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to the form')


@app.route('/calculate', methods=['POST'])
def calculate() -> 'html':
    G = float(request.form['G'])
    M = float(request.form['M'])
    T = float(request.form['T'])
    result = ley_kepler(G, M, T)
    title = "result kepler"
    return render_template('result.html',
                           the_G=G,
                           the_M=M,
                           the_T=T,
                           the_result=result,
                           the_title=title)


app.run(debug=True)