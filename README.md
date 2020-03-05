# Book Donation / Konyvkucko

## Table of Contents

1. [Summary](#Summary)

2. [Project purpose](#Project-purpose)

3. [UX](#ux)
    - [User stories](#User-stories)
    - [Admin stories](#Admin-stories)

4. [Design and colors](#Design-and-colors)
    
5. [Wireframes](#Wireframes)

6. [Features](#Features)

7. [Technology Used](#Technology-Used)

8. [Testing](#Testing)

9. [Credits](#Credits)

10. [DEPLOYMENT](#DEPLOYMENT)

11. [Disclaimer](#Disclaimer)

This is my third Milestone Project on the Full Stack Web Developer Code Institute course. For Data Centric Development module.

### Summary

I am the founder of Könyvkuckó, the Hungarian Children's Library in Ireland. My book collection is about 120 books, all our books were donated. I got books from authors, organizations, individuals. The launch of the Hungarian children's book was on the 29th of October, 2019. The books are hosted by Deansgrange Library, but they can be requested via the inter-library loans system from other libraries who are part of Libraries Ireland. The requested books will be delivered to the users' local library.

[Back to Top](#table-of-contents)

### Project purpose: 

The purpose of the project is to build a full-stack site that allows the users to manage a common dataset about a particular domain.

The application allows users to search Hungarian children's books, check the wishlist and donate books either from our wishlist or any book they want. Only the admin can add new books to the database, delete and edit the existing books.

The project has the following sections:

* Home page
Contains two background images and a short description.

* Books page
Contains all the available books, each book has a View button, for more information about the book. When admin is logged in they can see an Add Book button, and an Edit and a Delete button as well.

* Donation page
On the top of the page the user can see the I would like to donate a book button, and all the books that have been donated to the library, but haven't arrived yet. The admin can see two buttons next to the book, the first one is to move the book from the Donation list to the Books list when the book arrives, the second one is a Delete button, in case the book never arrives. There is a third button, which allows the admin to approve the book, making it visible to users on Donation page. I read about **Defensive Design** and wanted to check the information the users provided when filled the donation form.

* Wishlist
Contains all the books that we are currently looking for. Users can donate any of them by clicking to the button next to the book. If users decide to donate a book that is not on the list, they can click on the button on top of the page. Admin sees a third button, as they can add a new book to the Wishlist.

* Login / Register page
I needed an admin account to delete/edit/add books, this is why I created the Login page. Any user can register here, but at the moment registration does not have any advantages.

[Back to Top](#table-of-contents)

### UX

#### User stories:

* As a user I would like to know about the books that are available to borrow from Libraries Ireland

* As a user I would like to get from a book to the Library's homepage to borrow the book

* As a user I would like to be able to donate books to the Hungarian Collection

* As a user I would like to access the Wishlist to see which books are needed by the library

* As a user I would like to be able to contact Konyvkucko with my questions

#### Admin stories:

* As an admin I would like to be able to add books to the collection and delete/ edit them

* As an admin I want to be sure that I approve all the books which appears on our donation page

* As an admin I want to be able to move books from wishlist to donation list

[Back to Top](#table-of-contents)

### Design and colors:

#### Fonts:

I used Nunito Sans, from Google Fonts

On fonts.google.com in the about section the description of the font is the following: Nunito is a well balanced sans serif typeface superfamily, with 2 versions: The project began with Nunito, created by Vernon Adams as a rounded terminal sans serif for display typography. Jacques Le Bailly extended it to a full set of weights, and an accompanying regular non-rounded terminal version, Nunito Sans.

Sans-serif is used as the default backup font in case when Nunito Sans was not possible to load.

#### Colors:

* ![#4284A4](https://placehold.it/15/4284A4/000000?text=+) #4284A4 - Primary background color

* ![#60a0bf](https://placehold.it/15/60a0bf/000000?text=+) #60a0bf - Button hover color, Form input field label color, Datepicker hover color

* ![#5B8BA3](https://placehold.it/15/5B8BA3/000000?text=+) #5B8BA3 - 404 page text block background color

[Back to Top](#table-of-contents)

### Wireframes:

#### Initial Wireframes:

Originally on the home page I wanted to have one background picture and 3 of our latest donated books, but then I discovered Parallax (Materialize). Parallax is an effect where the background image is moved at a different speed than the foreground content while scrolling, so I decided to use Parallax instead.

[Mobile View - Home](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/wireframes/initial_design_mobile_home.pdf)

[Mobile View - Donation](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/wireframes/initial_design_mobile_donation.pdf)

[Desktop View - Home](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/wireframes/initial_design_desktop_home.pdf)

[Desktop View - Donation](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/wireframes/initial_design_desktop_donation.pdf)


#### Final Wireframes:

[Mobile View - Home](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/wireframes/final_design_mobile_home.pdf)

[Mobile View - Donation](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/wireframes/final_design_mobile_donation.pdf)

[Mobile View - Books](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/wireframes/final_design_mobile_book.pdf)

[Mobile View - Books Admin View](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/wireframes/final_design_mobile_book_admin_view.pdf)

[Desktop View - Home](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/wireframes/final_design_desktop_home.pdf)

[Desktop View - Donation Admin View](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/wireframes/final_design_desktop_donation_admin_view.pdf)

[Desktop View - Books](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/wireframes/final_design_desktop_book.pdf)

[Desktop View - Books Admin view](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/wireframes/final_design_desktop_book_admin_view.pdf)

[Back to Top](#table-of-contents)


### Features:

#### Open Graph (OG):

I shared Konvkucko's link with Messenger as I wanted the app to be tested on more different devices. When a link is shared there is a nice feature: a little preview of the link’s content, with title, short description and an image of the designated page. This data comes from scraping the link for `Open Graph (OG)` data. I added og meta tags to my base.html and used Sharing Debugger (facebook developer tools) to debug.

#### Link to Ireland Libraries

On Books page user can check more details about each book by clicking the `View` button next to the book. This leads the user to the book detail page, where the `Borrow this book!` button takes the user to Libraries Ireland page, and after login user can request the book.

#### Features Left to Implement:

* As the application is about Hungarian books, for Hungarian families living in Ireland I plan to translate it Hungarian.

* I would like to add a search bar, where users can search books by author, title and age category.

[Back to Top](#table-of-contents)

### Technology Used:

* Required: HTML, CSS, JavaScript, Python+Flask, MongoDB

#### Languages, Frameworks, Editors & Version Control:

* HTML5
* CSS3
* JavaScript
* Python
* <a href="https://materializecss.com/"> Materialize Framework:</a> Used  the Materialize framework for grid system, structuring layout, cards, forms, button styling and responsive navigation bar.
* <A href="https://palletsprojects.com/p/flask/">Flask</a> Used Flask framework to compile modules and libraries.
* jQuery: Used to initialize elements of Materialize framework. For the home page (Parallax), Navbar collapse, datepicker.
* VSCode: Was used as a code editor.
* Git: Version control.
* <a href="https://github.com">Github</a> Used as a Git repository hosting service
* <a href="https://www.heroku.com/">Heroku</a> Is a container-based cloud Platform, I used Heroku to deploy this app.

#### Tools Used:

* <a href="https://www.mongodb.com/cloud/atlas">MongoDB</a> Is used to store the database in the cloud.
* <a href="https://fonts.google.com/specimen/Nunito">Google Fonts</a> Used Nunito Sans fonts
* <a href="https://www.favicon-generator.org/">Favicon Generator</a> Used to find the right Favicon for the project.
* <a href="https://compressjpeg.com/">compressjpg</a> Used to compress all my images.
* <a href="https://www.canva.com/photos/">Canva photos</a> Used to find the background images.
* <a href="https://validator.w3.org/">W3C Validator</a> Used to check the validity of my HTML and CSS.
* <a href="http://pep8online.com/">PEP 8 Online Validator</a> Used to check my Python code.
* <a href="https://moqups.com">moquaps</a> Used to create wireframes.
* facebook for developers: I used the [Sharing Debugger](https://developers.facebook.com/tools/debug/) to see the information that is used when my website content is shared on Facebook, Messenger and other places.

[Back to Top](#table-of-contents)

### Testing

Throughout the development of the project, I carried out testing. I used the Chrome Developer Tools consistently.

The application structure and mobile-first layout was tested on Google Chrome, Firefox and Safari. The application was tested on the following smartphone devices: Xiaomi, OnePlus6, iPhone11 and iPhone5. And on iPad and BMAX tablets.

#### Functionality Test

| Nr | Test          | Action | Before image  | After image  | Test result |
| ---|:-------------:| :----: | :-----:| :-----:| :-----:|
| 1 | Library Link | Click on: Borrow this book!  | ![Book detail page](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/static/images/Test/test1_library_link0.png) Book detail page| ![Library page](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/static/images/Test/test1_library_link1.png ) Library Link | Passed |
| 2 |  add_book |  https://konyvkucko.<br>herokuapp.com/<br>add_book  | ![add_book as admin](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/static/images/Test/test2_add_book_admin.png ) Admin|![add_book as non admin](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/static/images/Test/test2_add_book_not_admin.png ) Not Admin|Passed |
| 3 |  invalid book | https://konyvkucko.<br>herokuapp.com/<br>book_detail/5e | ![invalid book](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/static/images/Test/test3_invalid_book.png ) Admin | ![invalid book](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/static/images/Test/test3_invalid_book.png ) Not Admin  |  Passed |
| 4 |  insert_book | https://konyvkucko.<br>herokuapp.com<br>/insert_book | ![insert_book](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/static/images/Test/test4_insert_book.png ) Admin | ![insert_book](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/static/images/Test/test4_insert_book.png ) Not Admin  |  Passed |
| 5 |  wishlist | https://konyvkucko.<br>herokuapp.com/<br>wishlist | ![wishlist](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/static/images/Test/test5_wishlist_admin.png ) Admin | ![wishlist](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/static/images/Test/test5_wishlist_non_admin.png ) Not Admin  |  Passed |
| 6 |  donation | https://konyvkucko.<br>herokuapp.com/<br>donation | ![donation](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/static/images/Test/test6_donation_admin.png ) Admin | ![donation](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/static/images/Test/test6_donation_non_admin.png ) Not Admin  |  Passed |
| 7 |  books | https://konyvkucko.<br>herokuapp.com/<br>books | ![books](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/static/images/Test/test7_books_admin.png ) Admin | ![books](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/static/images/Test/test7_books_non_admin.png ) Not Admin  |  Passed |

#### Code Validation

* CSS was validated using W3C CSS Validation Service - Jigsaw, no errors were found.

* HTML was validated using W3C Markup Validation Service.

* Python code was validated using PEP8 online checker.

#### Defensive design

Defensive design was built into each template in app.py file.

* Only admin can add/ delete/ edit books, these buttons are hidden from users.

* Flash warnings were used when user entered already taken username at registration, or wrong password/username when signing in.

[Back to Top](#table-of-contents)

### Credits

* Book information (Summary, ISBN) are based on [Moly](https://moly.hu) 

* I used Datepicker from course mini project

* I use Materialize for card reveal (Books page), but wanted to change it to reveal the summary by hover.
I got the solution from stack overflow: https://bit.ly/39S4X6f It worked fine when I set it up, but after a while the cards were only revealed after clicking on them. The reason for this was that in main.js I put Datepicker code before the Card hover and there was an error in Datepicker, so the Card hover code was never reached.

#### Acknowledgements

* Special thanks to my friends who made me add extra validations to my app.py. Originally when a user wanted to donate us a book and filled the form, the book was visible on the Donation page. I created an approved function, and now admin approval is needed before any new books are displayed. I also check if user is signed in and is admin, before they could add/ delete/ edit a book.

* Many thanks to my mentor, Brian Macharia for support and advice throughout the project. You became my mentor when I started this milestone project and you always made sure to find the time for a mentor session when I needed you. Thank you!

[Back to Top](#table-of-contents)

### DEPLOYMENT

#### CLONINNG - GITHUB 

1. Follow this link to my [Repository on Github](https://github.com/taikatta/Milestone3-Konyvkucko) and open it.
2. Click `Clone or Download`.
3. In the Clone with HTTPs section, click the `copy` icon.
4. In your local IDE open Git Bash.
5. Change the current working directory to where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied earlier.
7. Press enter and your local clone will be ready.
 

#### DEPLOY TO HEROKU 

1. On Heroku create an account and log in.
2. Click `new` and `create new app`.
3. Choose a unique name for your app, select region and click on `Create App`
4. Under the `Settings` click `Reveal Config Vars` and set IP to 0.0.0.0 and the PORT to 5000
5. Go to the CLI and type `$ sudo snap install --classic heroku`
6. Type `$ heroku login` command into the terminal
7. Create `requirements.txt` ($ sudo pip3 freeze --local > requirements.txt)
8. Create a `Procfile` (`$ echo web: python app.py > Procfile`)
9. Go back to Heroku, under `Deploy` find `Existing Git repository` and copy the command:`$ heroku git:remote -a <app_name>` Paste this into the terminal.
10. (If repository was not created already, type:
11. `$ cd my-project/`
12. `$ git init`
13. `$ heroku git:remote -a <app_name>`)
14. Type `$ heroku ps:scale web=1` into the terminal.
15. Go back to Heroku, and at `Settings` copy `https://<app_name>.herokuapp.com/` 
16. In the terminal type `git remote add http://<app_name>.herokuapp.com/`
16. Type `git push -u heroku master`
17. In the app dashboard, under `Settings` click on `Reveal Config Vars`
21. Set "MONGO_URI" and "MONGO_DBNAME" and "SECRET_KEY"
22. Once the build is complete, go back to Heroku and click on `Open App`

[Back to Top](#table-of-contents)

### Disclaimer

This project was created for educational use only.

[Back to Top](#table-of-contents)