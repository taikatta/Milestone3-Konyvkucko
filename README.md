# Book Donation / Konyvkucko

## Table of Contents

1. [Summary](#Summary)

2. [Technology Used](#Technology-Used)

2. [Project purpose](#Project-purpose)

3. [UX](#ux)
    - [Strategy Plane](#strategy-plane)
    - [Scope Plane](#scope-plane)

4. [Features](#features)
    - [Existing Features](#existing-features)
    
5. [Technologies Used](#technologies-used)

6. [Testing](#testing)

7. [Deployment](#deployment)

8. [Credits](#credits)

This is my third Milestone Project on the Full Stack Web Developer Code Institute course. For Data Centric Development module.

### Summary

I am the founder of Könyvkuckó, the Hungarian Children's Library in Ireland. My book collection is about 120 books, all our books were donated. I got books from authors, organizations, individuals. The launch of the Hungarian children's book was on the 29th of October, 2019. The books are hosted by Deansgrange Library, but they can be requested via the inter-library loans system from other libraries who are part of Libraries Ireland. The requested books will be delivered to the users' local library.

#### Project purpose: 

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

## UX

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

#### Design and colors:

#### Fonts:

I used Nunito Sans, from Google Fonts

On fonts.google.com in the about section the description of the font is the following: Nunito is a well balanced sans serif typeface superfamily, with 2 versions: The project began with Nunito, created by Vernon Adams as a rounded terminal sans serif for display typography. Jacques Le Bailly extended it to a full set of weights, and an accompanying regular non-rounded terminal version, Nunito Sans.

Sans-serif is used as the default backup font in case when Nunito Sans was not possible to load.

#### Colors:

* ![#4284A4](https://placehold.it/15/4284A4/000000?text=+) #4284A4 - Primary background color

* ![#60a0bf](https://placehold.it/15/60a0bf/000000?text=+) #60a0bf - Buuton hover color, Form input field label color, Datepicker hover color

* ![#5B8BA3](https://placehold.it/15/5B8BA3/000000?text=+) #5B8BA3 - 404 page text block background color


#### Wireframes:

#### Initial Wireframes:

Originally on the home page I wanted to have one background picture and 3 of our latest donated books, but then I discovered Parallax (Materialize). Parallax is an effect where the background image is moved at a different speed than the foreground content while scrolling, so I decided to use Parallax instead.

[Mobile View - Home](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/Wireframes/initial_design_mobile_home.pdf)

[Mobile View - Donation](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/Wireframes/initial_design_mobile_donation.pdf)

[Desktop View - Home](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/Wireframes/initial_design_desktop_home.pdf)

[Desktop View - Donation](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/Wireframes/initial_design_desktop_donation.pdf)


#### Final Wireframes:

[Mobile View - Home](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/Wireframes/final_design_mobile_home.pdf)

[Mobile View - Donation](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/Wireframes/final_design_mobile_donation.pdf)

[Mobile View - Books](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/Wireframes/final_design_mobile_book.pdf)

[Mobile View - Books Admin View](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/Wireframes/final_design_mobile_book_admin_view.pdf)

[Desktop View - Home](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/Wireframes/final_design_desktop_home.pdf)

[Desktop View - Donation Admin View](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/Wireframes/final_design_desktop_donation_admin_view.pdf)

[Desktop View - Books](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/Wireframes/final_design_desktop_book.pdf)

[Desktop View - Books Admin view](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/Wireframes/final_design_desktop_book_admin_view.pdf)

## Features:

* facebook for developers I used the [Sharing Debugger](https://developers.facebook.com/tools/debug/) to see the information that is used when my website content is shared on Facebook, Messenger and other places.

#### Features Left to Implement:

## Technology Used:

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
* <a href="https://fonts.google.com/specimen/Nunito">Google Fonts</a>Used Nunito Sans fonts
* <a href="https://www.favicon-generator.org/">Favicon Generator</a> Used to find the right Favicon for the project.
* <a href="https://compressjpeg.com/">compressjpg</a> Used to compress all my images.
* <a href="https://www.canva.com/photos/">Canva photos</a> Used to find the background images.
* <a href="https://validator.w3.org/">W3C Validator</a> Used to check the validity of my HTML and CSS.
* <a href="http://pep8online.com/">PEP 8 Online Validator</a> Used to check my Python code.
* <a href="https://moqups.com">moquaps</a> Used to create wireframes.

## Testing

#### Operational Test

## Credits

#### Media

#### Acknowledgementsg

## Deployment
