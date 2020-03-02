import os
import sys
from bcrypt import checkpw, gensalt, hashpw
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask import (Flask, flash, redirect, render_template,
                   request, session, url_for)


if os.path.exists("env.py"):
    import env

app = Flask(__name__)
try:
    app.config["MONGO_DBNAME"] = os.getenv('MONGO_DBNAME')
    app.config["MONGO_URI"] = os.getenv('MONGO_URI')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
except Exception:
    sys.exit(1)

mongo = PyMongo(app)


@app.route('/')
def home():
    return render_template("home.html", title='Home')


@app.route('/books')
def allbooks():
    return render_template("books.html", books=mongo.db.books.find())


@app.route('/add_book')
def add_book():
    return render_template('addbook.html', title='Add Book')


@app.route('/insert_book', methods=['POST'])
def insert_book():
    books = mongo.db.books
    we_have_it = mongo.db.books.find_one({'ISBN': request.form['ISBN']})
    if we_have_it:
        books.replace_one({'_id': ObjectId(we_have_it['_id'])}, {
            'book_title': we_have_it['book_title'],
            'author': we_have_it['author'],
            'age_range': we_have_it['age_range'],
            'book_cover': we_have_it['book_cover'],
            'summary': we_have_it['summary'],
            'ISBN': we_have_it['ISBN'],
            'nm_of_copies': (int(we_have_it['nm_of_copies'])
                             + int(request.form['nm_of_copies'])),
            'last_donated': we_have_it['last_donated']
        })
    else:
        books.insert_one({
            'book_title': request.form['book_title'],
            'author': request.form['author'],
            'age_range': request.form['age_range'],
            'book_cover': request.form['book_cover'],
            'summary': request.form['summary'],
            'ISBN': request.form['ISBN'],
            'nm_of_copies': request.form['nm_of_copies'],
            'last_donated': request.form['last_donated']
        })
    return redirect(url_for('allbooks'))


@app.route('/edit_book/<book_id>')
def edit_book(book_id):
    the_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template('editbook.html', book=the_book)


@app.route('/update_book/<book_id>', methods=["POST"])
def update_book(book_id):
    books = mongo.db.books
    books.replace_one({'_id': ObjectId(book_id)}, {
        'book_title': request.form.get('book_title'),
        'author': request.form.get('author'),
        'age_range': request.form.get('age_range'),
        'book_cover': request.form.get('book_cover'),
        'summary': request.form.get('summary'),
        'ISBN': request.form.get('ISBN'),
        'nm_of_copies': request.form.get('nm_of_copies'),
        'last_donated': request.form.get('last_donated')
    })
    return redirect(url_for('allbooks'))


@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    mongo.db.books.delete_one({'_id': ObjectId(book_id)})
    return redirect(url_for('allbooks'))


@app.route('/donation')
def book_donation():
    return render_template("donation.html", donation=mongo.db.donation.find())


@app.route('/wishlist')
def wishlistpage():
    return render_template("wishlist.html", wishlist=mongo.db.wishlist.find())


@app.route('/donate_book/<book_id>')
def donate_book(book_id):
    the_book = mongo.db.wishlist.find_one({"_id": ObjectId(book_id)})
    return render_template('donatebook.html', book=the_book)


@app.route('/update_donation/<book_id>', methods=["POST"])
def update_donation(book_id):
    mongo.db.wishlist.delete_one({'_id': ObjectId(book_id)})
    donation = mongo.db.donation
    donation.insert_one({
        'author': request.form['author'],
        'book_title': request.form['book_title'],
        'ISBN': request.form['ISBN'],
        'approved': False,
        'book_cover': request.form['book_cover'],
        'contact_name': request.form['contact_name'],
        'contact_info': request.form['contact_info']
    })
    return redirect(url_for('thanks'))


@app.route('/add_to_books/<book_id>')
def add_to_books(book_id):
    the_book = mongo.db.donation.find_one({"_id": ObjectId(book_id)})
    return render_template('addtobooks.html', book=the_book)


@app.route('/insert_donation/<book_id>', methods=['POST'])
def insert_donation(book_id):
    mongo.db.donation.delete_one({'_id': ObjectId(book_id)})
    books = mongo.db.books
    books.insert_one({
        'book_title': request.form['book_title'],
        'author': request.form['author'],
        'age_range': request.form['age_range'],
        'book_cover': request.form['book_cover'],
        'summary': request.form['summary'],
        'ISBN': request.form['ISBN'],
        'nm_of_copies': request.form['nm_of_copies'],
        'last_donated': request.form['last_donated']
    })
    return redirect(url_for('allbooks'))


@app.route('/add_to_wishlist')
def add_to_wishlist():
    return render_template('addtowishlist.html', title='Add Book to Wishlist')


@app.route('/insert_to_wishlist', methods=['POST'])
def insert_to_wishlist():
    wishlist = mongo.db.wishlist
    wishlist.insert_one({
        'book_title': request.form['book_title'],
        'author': request.form['author'],
        'book_cover': request.form['book_cover'],
        'ISBN': request.form['ISBN']
    })
    return redirect(url_for('wishlistpage'))


@app.route('/add_to_donation')
def add_to_donation():
    return render_template('addtodonation.html', title='Add Book to Donation')


@app.route('/thanks')
def thanks():
    return render_template('thanks.html', title='Thank you')


@app.route('/insert_to_donation', methods=['POST'])
def insert_to_donation():
    donation = mongo.db.donation
    donation.insert_one({
        'book_title': request.form['book_title'],
        'author': request.form['author'],
        'book_cover': request.form['book_cover'],
        'ISBN': request.form['ISBN'],
        'approved': False,
        'contact_name': request.form['contact_name'],
        'contact_info': request.form['contact_info']
    })
    return redirect(url_for('thanks'))


@app.route('/approved/<book_id>')
def approved(book_id):
    donation = mongo.db.donation
    donation.update_one(
        {'_id': ObjectId(book_id)},
        {'$set': {'approved': True}}
    )
    return redirect(url_for('book_donation'))


@app.route('/book_detail/<book_id>')
def book_detail(book_id):
    the_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template('bookdetail.html', book=the_book)


# Error Handling of 404
@app.errorhandler(404)
def response_404(exception):
    return render_template('404.html', exception=exception)


@app.route('/userlogin', methods=['GET', 'POST'])
def userlogin():
    return render_template("login.html", title='Login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    login_user = mongo.db.users.find_one({'username': username})
    if login_user:
        if checkpw(
                request.form['password'].encode('utf-8'),
                login_user['password']):
            session['username'] = request.form.to_dict()['username']
            return render_template("home.html", title='Home')
        flash('Invalid username/password combination!')
        return render_template('login.html')
    flash('Invalid username/password combination!')
    return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    """Register user."""
    if request.method == 'POST':
        existing_user = mongo.db.users.find_one(
            {'username': request.form['username']}
        )
        if existing_user is None:
            hashpass = hashpw(
                request.form['password'].encode('utf-8'), gensalt())
            mongo.db.users.insert_one({
                'username': request.form['username'],
                'password': hashpass
            })
            session['username'] = request.form['username']
            return redirect(url_for('home'))
        flash('Sorry! This username already exists! Did you want to sign in?')
        return render_template('login.html')
    return render_template('register.html')


@app.route('/endsession')
def endsession():
    """End session."""
    session.clear()
    return render_template("home.html", title='Home')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', default=5000)),
            debug=True)
