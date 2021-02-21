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