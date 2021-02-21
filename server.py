from flask import Flask

# creates flask application, use to define routes
# or urls within the webserver
app = Flask(__name__)

# run the index function, the return statement
# will be what the web server return to the browser
@app.route('/')
def index0():
    return 'Hello, World!'

# 3 random numbers between 1 and 6 are shown
@app.route('/roll-dice')
def index():
    '''
    returns 3 random numbers between 1 and 6
    '''
    import random
    for x in range(3):
        return str(random.randint(1,7)) + str(random.randint(1,7)) + str(random.randint(1,7))