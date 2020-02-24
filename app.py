import os
from flask import Flask, render_template, redirect, request, url_for, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


app.config["MONGO_DBNAME"] = 'konyvkucko'
app.config["MONGO_URI"] = 'mongodb+srv://root:m0ng0database@myfirstcluster-ptc6u.mongodb.net/konyvkucko?retryWrites=true&w=majority'


mongo = PyMongo(app)

@app.route('/')
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


@app.route('/edit_book/<book_id>')
def edit_book(book_id):
    the_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template('editbook.html', book=the_book)


@app.route('/update_book/<book_id>', methods=["POST"])
def update_book(book_id):
    books = mongo.db.books

    books.update( {'_id' : ObjectId(book_id)},
    {
        'book_title': request.form.get('book_title'),
        'author': request.form.get('author'),
        'age_range':request.form.get('age_range'),
        'book_cover': request.form.get('book_cover'),
        'summary':request.form.get('summary'),
        'ISBN':request.form.get('ISBN'),
        'nm_of_copies':request.form.get('nm_of_copies'),
        'last_donated':request.form.get('last_donated')

    })

    return redirect(url_for('allbooks'))

@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    mongo.db.books.remove({'_id': ObjectId(book_id)})
    return redirect(url_for('allbooks'))

@app.route('/donation')
def book_donation():
    return render_template("donation.html", 
    donation=mongo.db.donation.find())

@app.route('/wishlist')
def wishlist():
    return render_template("wishlist.html", 
    wishlist=mongo.db.wishlist.find())


@app.route('/donate_book/<book_id>')
def donate_book(book_id):
    the_book = mongo.db.wishlist.find_one({"_id": ObjectId(book_id)})
    return render_template('donatebook.html', book=the_book)


@app.route('/update_donation/<book_id>', methods=["POST"])
def update_donation(book_id):
    mongo.db.wishlist.remove({'_id': ObjectId(book_id)})
    donation = mongo.db.donation
    
    donation.insert_one(
    {
        'author': request.form['author'],
        'book_title': request.form['book_title'],
        'ISBN':request.form['ISBN'],
        'book_cover': request.form['book_cover'],
        'contact_name':request.form['contact_name'],
        'contact_info':request.form['contact_info']
    })
    return redirect(url_for('book_donation'))


@app.route('/add_to_books/<book_id>')
def add_to_books(book_id):
    the_book = mongo.db.donation.find_one({"_id": ObjectId(book_id)})
    return render_template('addtobooks.html', book=the_book)

@app.route('/insert_donation/<book_id>', methods=['POST'])
def insert_donation(book_id):
    mongo.db.donation.remove({'_id': ObjectId(book_id)})
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


@app.route('/add_to_wishlist')
def add_to_wishlist():
    return render_template('addtowishlist.html', title='Add Book')


@app.route('/insert_to_wishlist', methods=['POST'])
def insert_to_wishlist():
    
    wishlist = mongo.db.wishlist
        
    wishlist.insert_one({
            'book_title': request.form['book_title'],
            'author': request.form['author'],
            'book_cover': request.form['book_cover'],
            'ISBN':request.form['ISBN']
        })
    return redirect(url_for('wishlist'))

@app.route('/book_detail/<book_id>')
def book_detail(book_id):
    the_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template('bookdetail.html', book = the_book)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
        port=int(os.environ.get('PORT', default=5000)), 
        debug=True)