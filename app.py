import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Konyvkucko'

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', default='127.0.0.1'), 
        port=int(os.environ.get('PORT', default=5000)), 
        debug=True)