from flask import Flask
from flask import render_template

# The following terminal commands runs the app
'''
export FLASK_APP=server.py
export FLASK_ENV=development
flask run
'''

# creates flask application, use to define routes
# or urls within the webserver
app = Flask(__name__)

# run the index function, the return statement
# will be what the web server return to the browser as html
@app.route('/')
def index0():
    return render_template('index.html', name='Brandon')

# 3 random numbers between 1 and 6 are shown as html
@app.route('/roll-dice')
def index():
    '''
    returns 3 random numbers between 1 and 6
    '''
    import random
    for x in range(3):
        result = str(random.randint(1,7)) + str(random.randint(1,7)) + str(random.randint(1,7))
        return render_template('dice.html', name='Brandon', results=result)

# Define a route that will display a form
@app.route('/my-first-form')
def my_first_form():
    return render_template('my-first-form.html')

# Define a route that handles the form submission:
from flask import request

@app.route('/make-greeting', methods=['POST'])
def handle_form_submission():
    name = request.form['name']
    title = request.form['title']

    greeting = 'Hello, '

    if title != '':
        greeting += title + ' '
    
    greeting += name + '!'

    return render_template('greeting-result.html', greeting=greeting)

# Define a route that will display a form
@app.route('/message-form')
def message_form():
    return render_template('message.html')

@app.route('/message', methods=['POST'])
def handle_form_input():
    from model import predict
    
    textmsg = request.form['textmsg']
    
    result = predict(textmsg)

    return render_template('text-result.html', textmsg=textmsg, result=result)