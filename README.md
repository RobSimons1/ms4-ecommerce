[![Build Status](https://travis-ci.org/RobSimons1/ms4-ecommerce.svg?branch=master)](https://travis-ci.org/RobSimons1/ms4-ecommerce)

# Blindside-Brewing Site 

This Full-Stack site is designed to allow the user to peruse and purchase products available form Blindside Brewing that are stored in the Django database. 
In the cart section the of the site, the user is able to create, locate, display, edit and delete items in the cart in line with CRUD functionality. 
The user needs to be registered and logged in, in order to advance to the checkout page of the site where card details can be entered and payments 
made using STRIPE. 

The site is easy to use and allows the authenticated user a range of options including the ability to send an email to the site owner using the contact 
form and view and update their own profile. The user can leave a review for each product and view reviews left by other users.

The purpose of the site is to ultimately to sell Blindside Brewing products and make the user experience as easy and pleasurable as possible.

The link for the app is: 

*http://blindside-brewing.herokuapp.com/*

The link for the Github repository is:

*https://github.com/RobSimons1/ms4-ecommerce*

## UX

In order to make the user experience as easy and enjoyable as possible I opted for a simple looking site that is easy to navigate using the 
navigation bar buttons Shop, Register, Log In and Cart for the unathenticated user and Shop, Contact, Profile, Log Out and Cart for the 
authenticated user. Django provides a useful notification bar below the Navbar that alerts the user to when an action such as logging in or 
out is successful.

There is a search bar below the Navbar that the user can type in any word to search the products currently available. Each of the Blindside Brewing 
logos in the header and the footer act as links to the homepage and there are active links to Blindside Brewings Facebook, Twitter and Instagram 
pages in the footer. 

The user must be registered and logged in in order to make an actual purchase on the site. To register the user needs to complete the registration form 
on the registration page which requests a Username, Email address, Password and Password confirmation. The user also must confirm that they are over the 
legal drinking age by checking the Yes button. Once this is checked the `Create Account` button becomes live allowing the user to continue on the Shop / 
homepage provided the rest of the form is completed correctly. 

If the user wishes to add a product to their shopping cart they can do so by selecting the quantity field in the individual product paneland either using
the up / down arrows or inputing a number and pressing the `Add` button. This will add the specified quantity to the cart the total items is visually 
displayed on the cart icon in the navbar. The user can then select the Cart page that diplays the selected products, quantities and total price. The user 
can adjust the quantity in the quantity field and pressing the `Amend` button. If the value is set to zero the specified product will be deleted from the 
cart. If the user is happy with the products and quantities in their cart, they can proceed to the Checkout page using the `Checkout` button. Here the 
chosen products and total price are shown. The user can input their card payment details and in the Payment Details fields provided. then press the 
`Submit Payment` button. Provided the payment is successful the user will be redirected to the hompage and a green notification banner will be diplayed 
telling the user that they have successfully paid.  

The original concepts for the web-app pages can be seen in the *supporting_docs folder* under *blindside_brewing_database_schema.png*, 
*wireframe1_product_page.png*, *wireframe2_login_page.png*, *wireframe3_register_page.png*, *wireframe4_cart_page.png* and *wireframe5_checkout_page.png*. 
These were created in Balsamiq. There are numerous changes since these  wireframes, mainly due to learning more about the capabilities of Python and Django. 
There is also a database scehma showing the original idea for the project.

The site is aimed at users who have an interest in craft beers and it is hope that the success of the company will increase by having an online facility for 
customers to purchase their products. 

## Features

### Existing Features

The choice of features, links and buttons available to the user are:

* **Nav Bar –** Contains Blindside Brewing logo that is also a homepage link. The Navbar is designed to dissapear when the user scrolls down 
and reappear wehn the user scrolls up. This is a defensive mobile first design that allows a better view of the actual page (e.g. Shop page) on 
smaller screens.

* **Unauthorised User Nav Bar –** Contains Blindside Brewing logo that is also a homepage link. The Navbar links available to the unauthorised 
user are Shop, Register, Login and Cart. This is a limmited range of links that allows the the user to peruse the available products, but mainly
directs the user towards either logging via the Login page or registering via the Registration page. The links are hilighted and pulse when they 
are hovered on to make it clear to the user that they are links. Also, the current page that the user is on is highlighted in the Navbar for ease 
of navigation.

* **Authorised User Nav Bar –** Contains Blindside Brewing logo that is also a homepage link. The Navbar links available to the authorised 
user are Shop, Contact, Profile, Log Out and Cart. These links are designed to allow the user thorough interaction with the site and communication 
with the site owner. The links are hilighted and pulse when they are hovered on to make it clear to the user that they are links. Also, the current 
page that the user is on is highlighted in the Navbar for ease of navigation.

* **Side Nav Bar –** This becomes available on smaller screen types and is present in the form of the radio style menu icon in the top right 
corner of the Navbar. Once the icon is clicked the Side Navbar presents itself with all the links that are hidden in smaller view dependant on the 
users authorisation status that direct the user to the specified page. The links are highlighted and pulse when hovered on to make it clear to the 
user that they are links. The Navbar is designed to dissapear when the user scrolls down and reappear wehn the user scrolls up. This is a defensive 
mobile first design that allows a better view of the actual page (e.g. Shop page) on smaller screens.

* **Mission Statement –** This paragraph located below the Navbar on larger screen resolutions gives a brief synopsis of Blindside Brewing. What they do
and when they began. 

* **Search Bar –** The Search bar is available on all pages for the user to search for a specific beer by name. This has been included, as it is expected 
that eventually there will be a vast amount of products on the site. 

* **Individual Product Panels –** Each individual product has its own panel, inwhich the information stored in the database is presented for each 
specific product (e.g. Name, Description, Info, Blurb, Size, Alcohol, Price and Image). The user can input the quantity they require for each product 
and press the `Add` button, to add items to the Cart.

* **Footer –** The Footer is defensively designed to show only the active social links (Facebook, Twitter and Instagram) on smaller screen sizes. The 
larger screen resolutions show another homepage Blindside Brewing logo link and the Copyright info. The background for the fixed footer was left opaque, 
as again this allows the user to view more of the page and use more of the input fields on smaller resolutions.  

* **Success Message Bar –** When the user performs an action that requires confirmation, such as logging in or out, or sending a message via the contact 
form, a green notification banner will appear below the Navbar to tell the user that the operation was successfull.

* **Register Page –** The registration page allows the user to register with the site by providing a username, email address, password and password 
confirmation. They will also need to confirm that they are over the legal drinking age by checking the `Yes` radio button, which in turn activates the 
`Create Account` button. If the user already has an account, they can use the `Sign In` link at the top of the page. 

* **Login Page –** The Login page provides the user with a form where they can login using their username or email and password. There is a link for the user 
if they have forgotten their password that takes them to the Django Password reset page. On this page the user inputs their email address and an email is then 
sent to them allowing them to reset their password and then login to the site. There is also a `Don't have an account?` link that takes the user to the 
registration page.

* **Cart Page –** If there are no items in the Cart and the user selects the Cart page, they will be presented with a message saying 'No items in your cart' 
and a `Continue Shopping` button that redirects back to the Shop page. If the user has items in thir cart they will be displayed in the Cart page along with 
the options to `Amend` the quantity, `Checkout`, or `Continue Shoppping`. The total of the users cart is shown. If the user amends a products quantity to zero,
the item will be removed from the cart. Once an item is added to the cart the total quantity is displayed on the Cart icon in the Navbar. If the user is not 
authorised and selects the `Checkout` button, they will be redirected to the Login page.

* **Contact Page –** The Contact page allows the user to send a message to the site owner by completing the form that requests the users email and message. This 
is forwarded directly to the site owner and the user is notified by a green notification success message banner. 

* **Profile Page –** The Profile page allows the registered user to insert their name and address credentials, in order that these details can be prepopulated 
within the Users Checkout Form.  

* **User Review for a specified product page –** Within each individual product panel is an option to view the Reviews. Once the link is clicked, the user will be 
taken to the user_ratings page that lists all of the previous reviews about that specific product. These reviews display the Name (if user is registered, their 
Username); Review of the selected product; Rating out of five; Date / Time of review.  

* **Add User Review for a specified product page –** On this page the User has the choice of three fields. If the user is registered and logged in, the 'Name' field 
is pre-populated with the uername of the User. Once the Review and Rating fields are complete and submitted, the User's review will be saved to the database and 
presented in the Reviews page.

* **Logout Navbar Button –**  If pressed the user will be logged out from the site and all items in the cart will dissapear, as the user is taken back to the 
unathorised user homepage. The user is notified by a green notification success message banner that they have successfully logged out. 

### Features left to implement

* User can view each category and associated words separately by clicking `category name`. This will bring up all words under one category.

* User can currently input upper and lower case versions of the same into `word` and `category`. Possibly implementing a `Text Index` will fix this?

## Technologies Used
The languages, frameworks, libraries and other tools utilised for building this web-app are:

* **Gitpod -** Gitpod is a cloud-based integrated development environment (IDE) that has been used to write, run, and debug the code used for 
the web-app. https://www.gitpod.io/

* **GitHub -** GitHub has been used for version control of the code by using Git functions in the control panel. Github was utilised frequently 
during the development of the web-app.  https://github.com/

* **Heroku -** This is a cloud based application platform that allows deployment of an application to the web and connection to the database. 
https://heroku.com/

* **SQlite3 -** SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. 
SQLite is the most used database engine in the world. https://www.sqlite.org/index.html

* **PostgreSQL -** PostgreSQL is a powerful, open source object-relational database system. https://www.postgresql.org/

* **Django 1.11.29 -** Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. 
https://www.djangoproject.com/

* **Travis CI 4.3.0 -** Built to integrate with GitHub and Heroku. Using OAuth for authentication. Travis syncs users permissions to the repositories 
you want them to have access to. Allowing  greater control over security and to scale out your build infrastructure as needed.

* **AWS S3 -** Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, 
security, and performance. https://aws.amazon.com/s3/

* **Balsamiq -** fUsed for design of ireframes. https://balsamiq.com/

### Front-End Technologies

* **HTML 5 -** The web-app uses HTML5 as a fundamental basis for building the web-app. Where possible semantic HTML is used to give the user a 
better understanding.

* **CSS3 -** The web-app uses CSS3 for styling of elements within the website. It is linked from the page to the *style.css* file.

* **Bootstrap 3.7.7 -** The open-source Bootstrap framework has been used to implement the layout of the site. Bootstrap is also utilised 
to accommodate the responsive and mobile first design of the dashboard. https://getbootstrap.com/

* **Django-forms-bootstrap 3.1.0 -**  A simple bootstrap filter for Django forms. Extracted from the bootstrap theme.
https://django-bootstrap3.readthedocs.io/en/latest/

* **JavaScript -** The web-app uses Javascript to provide dynamic interactivity, as it is a full-fledged versatile programming language.
https://www.javascript.com/

* **jQuery -** The web-app uses jQuery, as it simplifies a lot of complicated tasks from JavaScript, such as AJAX calls and DOM manipulation. 
https://www.jquery.com/jquery-3.4.1

* **Google Fonts-** The dashboard uses Google fonts to accentuate certain text. https://fonts.google.com/

### Back-End Technologies

* **Python 3.1 -** Python emphasises readability, uses English keywords and is highly extensible. The core language itself is quite small, 
and it is easy to learn for brginners. https://www.python.org/  

* **Gunicorn 20.0.4 -** Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX. The Gunicorn server is broadly compatible with 
various web frameworks, simply implemented, light on server resources, and fairly speedy. https://docs.gunicorn.org/en/stable/

* **Pillow 7.1.1 -** The Python Imaging Library adds image processing capabilities to your Python interpreter. This library provides
extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities. 
https://pillow.readthedocs.io/en/stable/handbook/overview.html

* **Psycopg2 2.8.5 -** Psycopg is the most popular PostgreSQL database adapter for the Python programming language. Its main features are 
the complete implementation of the Python DB API 2.0 specification and the thread safety. https://pypi.org/project/psycopg2/ 

* **boto3 1.14.5 -** Boto is the Amazon Web Services (AWS) SDK for Python. It enables Python developers to create, configure, and manage AWS 
services, such as EC2 and S3. https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

* **Jinja -** This is a modern and designer-friendly templating language for Python. It is fast, widely used and secure with the optional 
sandboxed template execution environment. https://jinja.palletsprojects.com/en/2.11.x/

* **Stripe 2.46.0 -** Checkout creates a secure, Stripe-hosted payment page that lets you collect payments quickly. It works across devices 
and is designed to increase conversion. Checkout makes it easy to build a first-class payments experience. 
https://stripe.com/docs/payments/checkout


## Testing

The main basic functions of the site that required rigorous testing in different scenarios are listed below.

*	**Navbar** 
    * All Navbar links are coded within the base.html that extends to each html page. The logo is a home link that has been tested form each page and each link 
    (e.g. `Shop`; `Register`; `Login`; `Cart`; `Contact`; `Profile`; `Logout`) works correctly accross all devices and screen resolutions. Each link directs the 
    user to the relevant page and the `Logout` button logs the user out of the site.
    

*	**Footer** 
    * All Footer links ar ecoded within the base.html that extends to each html page. The Footer Logo links back to the homepage that works from each page.
    The Footer Social Links of `Facebook`, `Twiter`and `Instagram` have all been extensively tested to redirect the user to the relevant Blindside Social Media 
    page.

*	**Search Bar** 
    * The Search bar is used to search all available products on the homepage. The search bar is available beneath the header on each individual page. The search
    bar returns items that are related to the search string, otherwise no items will be returned. This function works correctly.

*	**Product Panel**
    * Each product panel shows all information related to the individual product, the majority of which is stored in the database. Products can be added or deleted
    by a SuperUser in the `admin` panel. The attributes for each product displayed in each product panel are Name, Description, Info, Blurb, Size, Alcohol, Price 
    and Image. All of these attributes have been tested and work correctly. In Products/tests.py/ there is a test configured to test the product name, which works 
    as expected. 

*	**Review Link** 
    * Within each product panel their is a link to the User reviews page. This directs the user to a page that shows the customer reviews for that specific product. 
    This function has extensively tested and returns all the user reviews and ratings in chronological order.  

*	**User Reviews / Ratings Page**
    * Each Customer review returns the Name, Review, Rating out of 5 and the Date. All of these fields are stored in the Django database and linked to the individual 
    product by the Foreign Key and Primary Key. The Product.ID label is required for the function to work, but is hidden from view, as it displays the relevant number 
    ID associated with the particular product. The functionality for this feature works as expected. 

*	**Add a Review / Rating Page**
    * The `Add a review` link takes the user to the page where a review and reatin can be inserted in to the database. If the user is logged in the `Name` field will 
    be automatically populated with the users username, if not this will be blank and can be filled in. The review field s for the user to insert their thoughts of 
    the product. The rating allows the user to score the individual product between 1 and 5. All of these fields are stored in the Django database and linked to the 
    individual product by the Foreign Key and Primary Key. To test the funcionality of this feature extensive print statements were added to the `create_an_item` 
    function that checked that the form was valid and if so saved utilising Django's 'The Save() Method'.


*	**Quantity Denominator Field** 
    * This field inserts a selected number of each individual product into the Cart. Validation of this can be seen when the user presses the `Add` button and the number 
    quantity of items can be seen in the Cart Icon in the Navbar. This is the case on larger resolution screens, but notfor smaller resolutions where the Cart Menu Icon is 
    not immediately available. Once the user views the Cart page. all of the selected items will be shown with their aquired quantity.

*	**Registration Form** 

*	**Registration - Legal Age Checker** 

*	**Login Page** 

*	**Cart Page** 

*	**Cart - Amend Quantity Button** 

*	**Cart - Total Shopping Amount**

*	**Cart - Checkout Button** 

*	**Cart - Continue Shopping Button**

*	**Checkout Page**

*	**Checkout - Payment Details Form**

*	**Checkout - Payment Card Info Form**

*	**Checkout - Submit Payment Button**

*	**Contact Page**

*	**Contact - User Email Field**

*	**Contact - Message Field**

*	**Contact - Send Message Button**

*	**Profile Page - Form**

*	**Profile - Update Profile Button**



*	**W3 Nu Html Checker** 
    * All .html files require validation through the online checker. This ensures that the code is more legible and does 
      not contain formatting errors. https://validator.w3.org/ 

*	**W3C CSS Validator** 
    * The style.css file requires validation through the online checker. This ensures that the code is more legible and does 
      not contain formatting errors. https://jigsaw.w3.org/css-validator/validator

*	**PEP8 Online** 
    * The Python (.py) pages require validation through the online checker. This ensures that the code is more legible and does not contain formatting 
      errors. http://pep8online.com/            
       
The final database schema and desktop wireframes for the web-app can be seen in the *supporting_docs folder* under *blindside_brewing_database_schema.png*, 
*wireframe1_product_page.png*, *wireframe2_ Login_page.png*, *wireframe3_ register_page.png*, *wireframe4_ cart_page.png* and *wireframe5_ checkout_page.png*. 
These wireframes and database schema were used initially to plan the site and build around. The opinions of numerous people including my mentor, friends, 
tutors, chat forums and such like, whom were asked during various stages of the project.

## Issue List


  | Issue  |                 Description                     |       Solution                      |  
  | ------ |:-----------------------------------------------:|:-----------------------------------:|
  |   1    |Attempted to set up Text Index in app.py to allow search bar to function correctly following MongoDB Manual, but was unable to get this to work as db can only have ONE index, and by doing it in the python file, it will create an index per each search, and errors.|Instead used `$regex": query` method, which works for my data|
  |   2    |Results of search bar search not displaying all first letter cases (e.g. 'A'and 'a') |`case_sensitive=false` added to Python function|
  |   3    |Results of individual letter searches needed to ignore capitalisation of first letter |`letter='^A'` added to Python functions for each letter|
  |   4    |`More Links` tab in Footer is intended for external links such as FaceBook, Twitter etc. |Due to time constraints these links have not been set up|
  |   5    |Flashed message that appears when a user inputs a duplicate new Word or Category only appears for words and categories capitalised in the exact same way as already in the database |In order to correct this all words and categories would have to enter the database in the same case letters. Due to time constraints it was not possible to write this functionality|
  |   6    |Issues with some Materialize elements not able to target in CSS (e.g. Colour of individual letter Aa, Bb etc) |Had to leave in-line HTML (e.g. `a class="blue-grey-text"`|
  |   7    |Try to separate each different Letter in the `Browse Words` page, so that all words associated with that letter are listed under a title (e.g. Aa) |Jinja does not appear to have enough logic to complete this task, including seeing the difference between 'A' and 'a' for example.|
  |   8    |`Upvoting functionality`, where the  user is able to vote on a specific word, as intended in Wireframe4 and button in Wireframes Header |It appears that this is a function that requires Login/Authentification that I have not had time to implement these |
  |   9    |Login / Authentification` buttons as shown in wireframes |Due to time constraints, I was not abe to implement these|
  |   10   |Explorer displaying the |Decided to leave this, as browser being phased out and rarely used |
  |   11   |Switched IDE midway through project fron AWS Cloud9 to Gitpod |This was time slightly time consuming, as had to learn working of the new IDE |
  |   12   |Initially `Browse Words` page displayed words in case sensitive order, so that words beginning upper case would superseed words beginning lower case, no matter what the second letter of the word was |`case_sensitive=false` added to Python function|
  |   13   |Initially a link to an online store was planned in the Header of the Wireframes |Due to time constraints and possible Login / Authentification issues, this was not possible |
  |   14   |Needed to validate CSS for debugging purposes | Utilised jigsaw.W3 CSS Validator. one warning: Imported style sheets are not checked in direct input and file upload modes. This can be ignored, as a does not affect import or code |
  |   15   |Could not resize SideNav Radio Button to appear larger on smaller devices | Can target with CSS using `.button-collapse`, but can only change color. Have left this as general size and colouris adequate in smaller resolutions |
  |   16   |Needed to validate HTML in all .html pages for debugging purposes | Utilised W3 HTML Markup Validation Service, which returns multiple errors where the syntax '{}' has been used. This is Jinja that has been populated via flask. Therefore, it is not HTML and these errors can be ignored. The method used was to view the page source code in the web-app for each .html page and copy this code in to the validator, as it is pure HTML code. |
  |   17   |`Materalize` versus `W3 HTML Markup Validation Service`  |Only one main error in `W3 HTML Markup Validation Service`: `Error: Element div not allowed as child of element ul in this context`. The Materialize Official Documentation (https://materializecss.com/collapsible.html) allows `divs` within a `ul` for a `collapsible` element. Therefore, I have left these features in, as cannot find a better way to list the items without them overlapping (e.g. Word Results)|
  |   18   |Needed to validate Python (app.py) for debugging purposes| Utilised PEP8 online checker. All code successfully updated and passed |
  |   19   |Initially the `Wave picture` and `Basic Card` were going to appear on each page of the web-app, as in the Wireframes|Decided against this because it was unnecessary|
  |   20   |`Comments and Messaging service` originlly planned in Wireframes Footer  |Due to time constraints and possible Login / Authentification issues, this was not possible|
  |   21   |Are Python Flask and Jinja functions self explanatory |Added further comments to app.py file|
  |   22   |Is HTML semantic and self explanatory  | Added further comments to index.html file |
  |   23   |Blank form input | The User should not be able to input a blank form in to the database using the fields in `add_word` and `add_category`. Due to time constraints this prevntion haas not been implemented |
  |   24   |Issue with `Search Button` moving accross rows on smaller resolutions  | Utilised `col s3 offset-m1 offset-l2 center active` to make the `Search Bar` and `Search Icon` remain on the same row in all resolutions |
  |   25   |When inspecting smaller resolutions on a PC using `Dev Tools` there is a large amount of white space between the `Main Section` and the `Footer` | When tested on actual devices (e.g. iPhone 5/SE, iPhone 6/7/8), there was not the same large amount of white space. Therefore have left the Materialize margins as they are  |  
  |   26   |Finally, add non-test data in to the database  | web-app thoroughly tested in Heroku deployed version for `CRUD` functionality, by deleting test database inputs and inputting actual words, categories and definitions |

## Deployment

The web-site is designed in the Gitpod environment and regularly committed to GitHub after each crucial piece of coding. 
Using this method as a sanity check for the development enabled me to restore the site back to previous stages when it 
functioned correctly or easily find lost pieces of code. 

### To deploy the project to Github the following steps were taken:

  1. created a `master` branch in Github repository 
  2. Used Local AWS Cloud9 and Gitpod environment used to build the site
  3. Committed files to the staging area using bash terminal commands: `git status`; `git add (specify directory)`; `git commit -m"add message"`
  4. Pushed files to the working environment using `git push`, which then updates the repository.
  5. Published site from `master` branch using `settings` tab in the main page of the repository, select `source` as `master branch`, then `save`
  6. The repository can be cloned by clicking `Clone or Download` on the main page of the repository 
  7. In the Clone with HTTPs section, click the clipboard icon to copy the clone URL for the repository
  8. Open Git Bash Terminal
  9. Type `git clone`, and then paste the URL
  10. Press `Enter`. A local clone will be created.

### To set gitignore environment variables the following steps were taken: 

  1. Create a file named env.py in the root directory of your project. This is the file you will use to define your environment variables.
  2. If you don't have one already, create a file named .gitignore  in the root directory of your project.
  3. Next we need to stop git from pushing this file to github, and so keep your environment variables secret. To do this, open your .gitignore  file add the following text: env.py
  4. At the top of your env.py  file, you need to import os so that you can set the environment variables in the operating system. Once you have added the line “import os” 
     underneath you can assign your environment variables using the following syntax:  
     `os.environ["Variable Name Here"] = "Value of Variable Goes Here"`
  5. Then the following code imports this new env.py file where you need to use your environment variables. For example your app.py file for flask project. Add this under your 
     other imports at the top of the file  
     `from os import path`
      `if path.exists("env.py"):`
      `import env` 
  6. Now that your environment variables have been set in your env.py file, and the file has been imported into your project, you can use them as needed, for example using the following syntax:  
     `DATABASES = {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),}`

### To deploy the project to Heroku the following steps were taken:

  1. created a Heroku account @ https://signup.heroku.com/
  2. Create `requirements.txt` file in Gitpod workspace for Heroku to understand installation files to run app. From CLI type type 
     `pip3 freeze --local > requirements.txt`.
  3. To install the Heroku command line on Gitpod or AWS Cloud9, use the following command `npm install -g heroku`
  4. Using the `New` buton, Create a new app with apropriate title and server in Heroku. This creates a connection between the Gitpod application and Heroku that would allow us 
     to push our changes using Git to update the application at any given time. 
  5. To login to Heroku from the CLI, use the command `heroku login`
  6. To get the application up and running a `Procfile` is required that istructs Heroku which file is the entry point. Use the following command to create this: 
     `echo web: python app.py`
  7. Code that is prepared to be pushed from Github to Heroku can be executed following the CLI commands:
     `git add .`
     `git commit -m "fist Heroku commit"`
     `git push`
  8. Now that the relevant code is pushed to Github, it can also be pushed to Heroku from the chosen branch (e.g. Master)
  9. To connect an existing repository from Github to Heroku use the following CLI syntax: `heroku git:remote -a [followed by name of Heroku app]`
  10. To push to Heroku Master Branch, then simply use `git push heroku master`
  11. To scale dynos and run the app in Heroku, use the CLI command: `heroku ps:scale web=1`
  12. In order for the server instance on Heroku to know how to run our application, we need to specify a few Config Vars in Heroku. To do this go to `Settings` 
      tab > `Config Variables` and input: `AWS_ACCESS_KEY_ID`; `AWS_SECRET_ACCESS_KEY`; `DATABASE_URL`; `DISABLE_COLLECTSTATIC`; `EMAIL_ADDRESS`; `EMAIL_PASSWORD`
      `EMAIL_PASSWORD`; `SECRET_KEY`; `STRIPE_PUBLISHABLE`; `STRIPE_SECRET`.  
  13. The following syntax will need to be added to your settings.py file to access the SECRET KEY for the new database URL `DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}`
  14. The Database can then be migrated to the Heroku Postgres (postgresql) database using the the commands `mmakemigrations` and `migrate` from the command line.      
  15. Once the build in Heroku is complete, click the `Open app` button.
  16. Objects can then be added to the new postgres database using the Admin Panel and logging in with your superuser credentials.  

## Credits 

### Content

This README.md file is based on the Code Institute template.

### Media 

All images and logo's utilised have been displayed with the permisson of Blindside-Brewing.

Favicon – created using http://www.favicomatic.com/done

### Acknowledgments

I would like to thank all of the Code Insitute Tutors for there incredible patients and assitance and my mentor Anthony Ngene 
(https://github.com/tonymontaro) for his invaluable feedback, as supervisor for this project. 