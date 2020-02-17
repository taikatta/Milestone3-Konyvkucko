import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


app.config["MONGO_DBNAME"] = 'konyvkucko'
app.config["MONGO_URI"] = 'mongodb+srv://root:m0ng0database@myfirstcluster-ptc6u.mongodb.net/konyvkucko?retryWrites=true&w=majority'


mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def helloka():
    return 'home'

    
@app.route('/books')
def allbooks():
    return render_template("books.html", 
    books=mongo.db.books.find())


@app.route('/add_book')
def add_book():
    return render_template('addbook.html', title='Add Book')


@app.route('/insert_book', methods=['POST'])
def insert_book():
    
    books = mongo.db.books
        
    books.insert_one({
            'book_title': request.form['book_title'],
            'author': request.form['author'],
            'age_range':request.form['age_range'],
            'book_cover': request.form['book_cover'],
            'summary':request.form['summary'],
            'ISBN':request.form['ISBN'],
            'nm_of_copies':request.form['nm_of_copies'],
            'last_donated':request.form['last_donated']
        
        })
    return redirect(url_for('allbooks'))



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
        port=int(os.environ.get('PORT', default=5000)), 
        debug=True)