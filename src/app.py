#!/usr/bin/env python
# import flask

# app = flask.Flask(__name__)

# @app.route('/')
# @app.route('/hello/')
# def hello_world():
#     return 'Hello World!\n'

# @app.route('/hello/<username>') # dynamic route
# def hello_user(username):
#     return 'I have been Updated my friend %s!\n' % username

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')     # open for everyone

# Import the calculator module
from calculator import add, subtract, multiply, divide

# Example usage
num1 = 10
num2 = 5

# Call calculator functions
result_add = add(num1, num2)
result_subtract = subtract(num1, num2)

print(f"{num1} + {num2} = {result_add}")
print(f"{num1} - {num2} = {result_subtract}")

# You can call other functions from calculator.py similarly