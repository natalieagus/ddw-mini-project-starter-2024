from flask import render_template, send_from_directory, make_response
from app import application

@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html', title='Mini Project 1 Home')

@application.route('/ex1')
def exercise1():
    return render_template('ex1.html', title='Mini Project 1 Exercise 1')

@application.route('/ex2')
def exercise2():
    return render_template('ex2.html', title='Mini Project 1 Exercise 2')

@application.route('/js/<path:filename>') # dynamic route parameter syntax
def serve_js(filename):
    # Manually set the Content-Type for JavaScript files
    response = make_response(send_from_directory('static/__target__', filename))
    response.headers['Content-Type'] = 'application/javascript'
    return response