from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>', 200

@app.route('/print/<parameter>')
def print_parameter(parameter):
    print(parameter)
    return parameter, 200

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = [str(i) for i in range(parameter)]
    return '<br>'.join(numbers), 200

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return 'Error: Division by zero', 400
        result = num1 / num2
    elif operation == '%':
        if num2 == 0:
            return 'Error: Modulo by zero', 400
        result = num1 % num2
    else:
        return f"Unsupported operation '{operation}'", 400

    return f'{num1} {operation} {num2} = {result}', 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)

