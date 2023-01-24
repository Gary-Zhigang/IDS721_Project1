"""Helllo World!
Python program using Flask for a simple Calculator
GUI using the flask module
"""

# import Flask Library

from flask import Flask, render_template, request


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
            results = eval(expression)
            print(results)
        except Exception as e:
            message = """Oops! 
            Your expression syntax is incorrect!
            The full returned Traceback:
            """+str(e)
            return render_template('index.html', results=message)
        return render_template('index.html', results=results)



@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello World! I can make change at route: /change'

@app.route('/change/<dollar>/<cents>')
def changeroute(dollar, cents):
    print(f"Make Change for {dollar}.{cents}")
    amount = f"{dollar}.{cents}"
    result = change(float(amount))
    return jsonify(result)
    
    
@app.route('/100/change/<dollar>/<cents>')
def change100route(dollar, cents):
    print(f"Make Change for {dollar}.{cents}")
    amount = f"{dollar}.{cents}"
    amount100 = float(amount) * 100
    print(f"This is the {amount} X 100")
    result = change(amount100)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)
