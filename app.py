import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


app.config["MONGO_DBNAME"] = 'konyvkucko'
app.config["MONGO_URI"] = 'mongodb+srv://root:m0ng0database@myfirstcluster-ptc6u.mongodb.net/konyvkucko?retryWrites=true&w=majority'


mongo = PyMongo(app)

@app.route('/')
def hello():
    return 'Konyvkucko'

@app.route('/books')
def getbooks():
    return render_template("books.html", 
    books=mongo.db.books.find())


if __name__ =="__main__":
    app.run(host=os.environ.get('IP', default='127.0.0.1'), 
        port=int(os.environ.get('PORT', default=5000)), 
        debug=False)