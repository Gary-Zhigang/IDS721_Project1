"""Helllo World!
Python program using Flask for a simple Calculator
GUI using the flask module
"""

# import Flask Library

from flask import Flask, render_template, request
from ast import literal_eval


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    # return '<h1>Hi, Welcome to this session</h1>'


@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        x = request.form['x']
        # print(x)
        # if x is blank or
        if x == "":
            pass
        else:
            try:
                x = int(x)
            except:
                return render_template('index.html', results="Non string value passed to x\n Please Provide an integer value")
        expression = request.form['expression']
        try:
            # results = eval(expression)
            results = literal_eval(expression)
            print(results)
        except ZeroDivisionError as e:
            message = """Oops! 
            Your expression syntax is incorrect!
            The full returned Traceback:
            """+str(e)
            return render_template('index.html', results=message)
        return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
