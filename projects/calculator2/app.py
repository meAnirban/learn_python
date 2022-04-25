from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home_page():
    return render_template('index.html')


@app.route('/math', methods = ['POST'])
def math_operation():
    if (request.method == 'POST'):
        operation = request.form['operation']
        num1= float(request.form['num1'])
        num2= float(request.form['num2'])
        if (operation == 'add'):
            result = f'Summation of {num1} and {num2} = {num1 + num2}'
        if (operation == 'subtract'):
            result = f'Subtraction of {num1} and {num2} = {num1 - num2}'
        if (operation == 'multiply'):
            result = f'Multiplication of {num1} and {num2} = {num1 * num2}'
        if (operation == 'divide'):
            result = f'Division of {num1} and {num2} = {num1 / num2}'
        return render_template('results.html', result =result)


@app.route('/via_postman', methods = ['POST'])
def math_operation_via_postman():
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