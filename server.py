from flask import Flask

app = Flask(__name__)

@app.route('/')
def index0():
    return 'Hello, World!'

@app.route('/roll-dice')
def index():
    '''
    returns 3 random numbers between 1 and 6
    '''
    import random
    for x in range(3):
        return str(random.randint(1,7)) + str(random.randint(1,7)) + str(random.randint(1,7))