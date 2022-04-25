from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home_page():
    return "Home Page"


@app.route('/via_postman', methods = ['POST'])
def calculator():
    if (request.method == 'POST'):
        operation = request.json['operation']
        num1= float(request.json['num1'])
        num2= float(request.json['num2'])
        if (operation == 'add'):
            result = f'Summation of {num1} and {num2} = {num1 + num2}'
        if (operation == 'subtract'):
            result = f'Subtraction of {num1} and {num2} = {num1 - num2}'
        if (operation == 'multiply'):
            result = f'Multiplication of {num1} and {num2} = {num1 * num2}'
        if (operation == 'divide'):
            result = f'Division of {num1} and {num2} = {num1 / num2}'
        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)