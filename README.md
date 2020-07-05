[![Build Status](https://travis-ci.org/RobSimons1/ms4-ecommerce.svg?branch=master)](https://travis-ci.org/RobSimons1/ms4-ecommerce)

# Blindside-Brewing Web-Application 

This web-app is designed to allow the user to manipulate the data Oceanographic Dictionary records stored in MongoDB. The user is able to create, 
locate, display, edit and delete records in line with CRUD functionality. 

The web-app is easy to use and allows the user to input their own words, categories and definitions into the database. The user can search for 
existing words in the database, as well as display existing and new words. Also, the user is able to edit current words and categories, as well as 
delete them. 

The purpose of the web-app is to ultimately build a large database of Oceanographic words, categories and definitions that will allow people to better 
understand the oceanic environment and all of the associated elements.

The link for the app is: 

*http://blindside-brewing.herokuapp.com/*

The link for the Github repository is:

*https://github.com/RobSimons1/ms4-ecommerce*

## UX

In order to make the user experience as easy and enjoyable as possible I opted for a simple looking site that is easy to navigate 
using the navigation bar buttons (Home, Browse Words, New Word and Manage Categories). There is also a search bar within the Navbar 
that the user can type in any word to search, as well as individual letters that are themselves links to all words beginning with the 
selected letter. The user is also able to add a new word using the floating green button to the left of the Navbar, as well as utilise 
links provided in the card placed on the right of the homepage (Words, New Word and Categories). Additionally, there are a selection of 
links in the footer that will assist the user to easily navigate the pages. A paragraph in the center of the Homepage explains what the
web-app is about.

Once the user browses a word using any of the available search facilities, they can then see the category to which that word belongs, as 
well view the drop down definition by pressing the button. There are also button options to edit or delete the word. A warning will present 
it's self to the user if they press the delete button.

To add a word the user is taken to the Add Word page where they can select an appropriate category, input the word and input the definition.
the user then presses the Add Word button to submit the information to the database. The operation can also be cancelled using the cancel button.
Either action will return the user to the Browse Words page that is sorted in alphabetical order.

The Manage Categories page allows the user to view all categories in alphabetical order and then either delete or edit an existing category 
using the buttons provided or add a new Category that will be submitted to the database. If editing the category, the user has the option to 
either save their changes or cancel the operation. Again, if the delete button is pressed a warning message will be displayed. 

The original concepts for the web-app pages can be seen in the *supporting_docs folder* under *oceanic_dictionary_database_schema.png*, 
*wireframe1_oceanic_dictionary_home.png*, *wireframe2_ oceanic_dictionary_browse_words.png*, *wireframe3_ oceanic_dictionary_manage_categories.png* 
and unused *wireframe4_ oceanic_dictionary_manage_categories.png*. These were created in Balsamiq. There are numerous changes since these  wireframes, 
mainly due to learning more about the capabilities of Python, Flask and MongoDB. There is also a database scehma showing the original idea 
for the project.

The web-app is aimed at users who share an interest in the ocean and oceanographic words, particularly those who would like to understand 
the spelling or definition of a word, or to which oceanographic category it belongs. 

## Features

### Existing Features

The choice of features, links and buttons available to the user are:

* **Nav Bar –** Contains homepage link in the title of the page that is animated and highlited when the user hovers on it to draw atttention to 
the page title. Below the title is a floating Add Word button which will direct the user to the Add Word page. In the centre of the Navbar is a 
Search bar that the user is able to type any word in to and search the database, this is highlighted by the green search button. The search bar 
will bring up all words related to the specified search that are in the database. The Navbar links that are Home, Browse Words, New Word and Manage 
Categories. Direct the user to these specific pages. The links are hilighted and pulse when they are hovered on to make it clear to the user that 
they are links.

* **Side Nav Bar –** This becomes available on smaller screen types and is present in the form of the radio style menu icon in the top left 
corner of the Navbar. Once the icon is clicked the Side Navbar presents itself with all the links that are hidden in smaller view (e.g. Home, 
Browse Words, New Word and Manage Category) that direct the user to the specified page. The links are highlighted and pulse when hovered on  
to make it clear to the user that they are links.

* **Individual Letter Links –** Each letter of the alphabet is represented by it's upper and lower case character. The individual letters are 
highlighted when hovered over to make the user aaware that they are links. Once clicked the user will be directed to a page that shows all words 
beginning with the specified letter listed in alphabetical order. Form there the user can see the associated category and definition and edit or 
delete the words.

* **Wave Picture –** The picture of the wave is the basis for all the colours used in the web-app. All colours utilised are colour picked from 
the wave picture.

* **Homepage Paragraph –** This paragraph informs the user of the web-apps purpose by briefly explaining the many things that can be found in 
our oceans.

* **Basic Card –** The card has a second explanation of the web-app and tells the user what they are able to to do with regards to the functions 
available (e.g. browse, search, edit and delete words. Also, categories can be added, managed and edited). There are three links available to the 
user on the card, which are Words, New Word and Categories.

* **Footer –** The Footer has yet another brief paragraph explainin the web-app and its functionality, as well as links to Home, Browse Words, 
New Word and Manage Categories. These are available in the Footer on every ppage of the web-app.

* **Word Results –** When the user searches for a word using the search bar or the individual letters they are dircted to the Word Results page 
that will show all resultant words. Each word has it's own box and within the box is displayed the word in bold, as well as the associated Category.
then the word again.

* **Definition Button –** The large definition button and dropdown selector to its left in each individual word box will display the words definition 
in the drop-down when selected. This is so that the user can choose if they wish to see certain definitions and not all are displayed on screen at 
once. The button pulses when hovered on.

* **Edit Word Button –** The Edit button in each individual word box takes the user to the Edit Word page. Here the user is shown the existing details 
of the word from the database (e.g. Word Category, Input Word and Input Definition). The user is able to edit any of these details by then pressing 
the Edit Word button. There is also an opportinity to cancel the operation by pressing the Cancel button. Once the user either edits the word or cancels 
the operation, they are taken back to the Browse Words page. 

* **Delete Word Button –** The Delete Button in each individual word box gives the user the opportunity to delete the word and associated category from 
the database completely. Once pressed a message is diplayed asking the user if they are sure they want to delete this word?

* **Add Word –** When the user selects the Add Word green button in te Navbar or New Word from any of the links they will be taken to the Add Word page 
where they are given a blank form to fill in beginning with choosing a word category from the dropdown list, then inputting the word, followed by 
inputting the definition. Once the form is completed the user can submit the word to the database using the Add Word button or cancel the operation 
using the Cancel button. Either button will take the user back to the Browse Words page. If the user inputs a word that already exists in the database 
they will receive an error message stating "This item already exists in the database".

* **Categories –** When the user selects Manage Categories from the Navbar or any of the Categories links, they are taken to the Categories page. This 
page displays all of the existing categories in alphabetical order. 

* **Add Category Button –** This button directs the user to a page with a single line form where they can input the name of a new category. Once the 
form is completed the user can submit the category to the database using the Add Category button or cancel the operation using the Cancel button. 
Either button will take the user back to the Categories page. If the user inputs a category that already exists in the database they will receive an 
error message stating "This item already exists in the database". 

* **Delete Category Button –** The Delete Button to the left of each individual category on the Categories page gives the user the opportunity to delete 
the category from the database completely. Once pressed a message is diplayed asking the user if they are sure they want to delete this category?

* **Edit Category Button –** The Edit button to te far left of each individual category on the Categories page takes the user to the Edit Category page. 
Here the user is shown the existing category from the database. The user is able to edit this detail by then pressing the Edit Category button. There is 
also an opportinity to cancel the operation by pressing the Cancel button. Once the user either edits the category or cancels 
the operation, they are taken back to the Categories page. 

### Features left to implement

* User can view each category and associated words separately by clicking `category name`. This will bring up all words under one category.

* User can currently input upper and lower case versions of the same into `word` and `category`. Possibly implementing a `Text Index` will fix this?

* Individual words in `Browse Words` page to be spilt up into there own individual letter and not one continous list of all words in alphabeitical order. Could potentially add a `Back to Top` button after every Letter instance?

* User `LOGIN` and `REGISTER` options to be implemented for better security and traceability.

* `Back to top` button to be implemented in `Browse Words` page and `Categories` page to allow user to easliy return to the top of the page. 

* Voting on words Page with thumbs `up` and `down` functions detailed in Wireframe4. Difficult to implement without user login credentials.

* `Text Index` could improve overall user experience if implemented?

* `Comments` and `Messaging` services originally planned in Wireframes. Difficult to implement without user login credentials.

* Online `Store` originally planned in Wireframes. Difficult to implement without user login credentials.

* Currently the user is able to submit a `blank form` to the database. Would like to implement a flashed error message to prevent this.

## Technologies Used
The languages, frameworks, libraries and other tools utilised for building this web-app are:

* **Gitpod -** Gitpod is a cloud-based integrated development environment (IDE) that has been used to write, run, and debug the code used for 
the web-app. https://www.gitpod.io/

* **GitHub -** GitHub has been used for version control of the code by using Git functions in the control panel. Github was utilised frequently 
during the development of the web-app.  https://github.com/

* **Heroku -** This is a cloud based application platform that allows deployment of an application to the web and connection to the database. 
https://heroku.com/

* **Mongo DB Atlas -** This is a general purpose, document based, distributed database with scalability and flexability. https://www.mongodb.com/

* **PyMongo -** This is a Python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from 
Python, as an API for MongoDB intergration. https://api.mongodb.com/

### Front-End Technologies

* **HTML 5 -** The web-app uses HTML5 as a fundamental basis for building the web-app. Where possible semantic HTML is used to give the user a 
better understanding.

* **CSS3 -** The web-app uses CSS3 for styling of elements within the website. It is linked from the page to the *style.css* file.

* **Materialize 0.100.2 -** The open-source Materialize framework has been used to implement the layout of the web-app. Materialize is also 
utilised to accommodate the responsive and mobile first design of the web-app. http://archives.materializecss.com/0.100.2/about.html

* **JavaScript -** The web-app uses Javascript to provide dynamic interactivity, as it is a full-fledged versatile programming language.

* **jQuery -** The web-app uses jQuery, as it simplifies a lot of complicated tasks from JavaScript, such as AJAX calls and DOM manipulation. 
https://www.jquery.com/jquery-3.4.1

* **Google Fonts-** The dashboard uses Google fonts to accentuate certain text. https://fonts.google.com/

### Back-End Technologies

* **Python 3.1 -** Python emphasises readability, uses English keywords and is highly extensible. The core language itself is quite small, 
and it is easy to learn for brginners. https://www.python.org/  

* **Flask -** This is a lightweight Web Server Gateway Interface (WSGI) web application framework. There is little boilerplate code for 
getting a simple app up and running.

* **Jinja -** This is a modern and designer-friendly templating language for Python. It is fast, widely used and secure with the optional 
sandboxed template execution environment. 

* **dnspython -** This is a toolkit for Python that supports almost all record types and allows the new style connection string for MongoDB 
Atlas to be utilised.

* **Flask-PyMongo -** This allows Flask to communicate with Mongo. It is optimized to work with Flask.

* **itsdangerous -** This is used to cryptographically sign and customize how the data is serialised.

* **Werkzeug -** This is a comprehensive Web Server Gateway Interface (WSGI) web application library.

## Testing

The main basic functions of the web-app that required rigorous testing in different scenarios are listed below.

*	**Navbar** 
    * All Navbar links and buttons are coded within the Header section of the base.html with associated Python functions set up in app.py. 
    * Check Title link words (Oceanographic and Dictionary) return user to Homepage in every instance by ensuring that the index (/show_words) page is 
      returned to. This is valid for both the words 'Oceanographic' and 'Dictionary', as thay are split across two separate rows. 
    * Green `Add Word` button is configured to redirect the user to the Add Word page. Verified the link and left side positioning in all browsers and 
      screen sizes. 
    * The Search Bar required rigourous testing due to the varoius ways the words in Mongo DB could be accessed and displayed (See Issues List #1).
    * Green magnifying glass icon `Search` button next to the search bar activates the entry into the Search Bar. This has been tested and affixed in place 
      to maintain its funcionality in all browsers and screen sizes.
    * The Navbar `Home`, `Browse Words`, `New Word` and `Manage Categories` buttons have been extensively tested to rediriect the user to the relevant page.
    * The Side-Nav buttons of `Home`, `Browse Words`, `New Word` and `Manage Categories` have been extensively tested to rediriect the user to the relevant 
      page.

*	**Footer** 
    * The Footer links of `Home`, `Browse Words`, `New Word` and `Manage Categories` have all been extensively tested to redirect the user to the relevant page.
    * the `More Links` button is where links to external pages will be placed (e.g. Facebook, Twitter etc.) (See Issues List #4).

*	**Main base.html section**    
    * The Individual alphabetical letters are situated below the NavBar, but still appear on every page of the web-app. Each letter has been tested numerous 
      times to ensure that the functionality is correct and brings up all words begininng with the relevant letter, regardless of whether the word stored in the 
      database begins with an upper or lower case character.
    * A flashed message appears `This item aleady exists in the database` when a user inputs a word or category that is already in the database. This has been 
      tested and works provided that spelling and capitalisation of letters matches exactly what is all ready in the database (See Issues List #5).

*	**Homepage Main Section**    
    * Basic Card Links on the home page of `WORDS`, `NEW WORD` and `CATEGORIES` have been extensively tested to take the user to the relevant page.
    * The Wave image, homepage paragraph and basic card are set-up to maintain a third each of this section on larger screen types and each take up 
      the entire width of the screen on smaller devices.

*	**Browse Words Main Section**  
    * The words on this page are listed in alphabetical order regardless of the case of the initial letter. This functionality required extensive testing in order 
      make the functions work correctly.
    * The `Definition` button and drop down menu required were rigourously tested to ensure that they function correctly and display the correct definition for the 
      associated word direct from the data base.
    * The `Edit` button for each word redirects the user to the Edit Word page.  
    * The `Delete` button brings up the `Are you sure you want to delete this word??` box where the user can choose `Ok` or `Cancel`. The `Ok` button deletes the 
      word and associated definition from the database completely, which functonality has been thoroughly tested. `Cancel` returns the user to the Browse Words page.

*	**New Word Main Section**
    * The user is taken to the Add Word page, where there is a three row form. The `Choose Category` row is a drop down menu selector that shows all categories 
      currently entered in to the database. This drop down has been tested to ensure that it shows the categories in alphabetical order regardless of capitalisation
      of the initial letter.The `Input Word` and `Input Definition` rows have been thoroughly tested so that the functionality works and iputs a new word_id and 
      associated definition in to the database. This required a large amount of testing and with different functions and methods.
    * The `Add Word` button submits the form to the database and has been extensively tested.
    * The `Cancel` button returns the user to the Browse Words page. This has been thoroughly tested.

*	**Edit Word Main Section**
    * The `Edit Word` button directs the user to this page where the user is presented with a three row form. The form is already populated with the existing 
      `Word Category`, `Word Name` and `Word Definition` from the database. The `Word Category` row is a drop down menu selector that shows all categories 
      currently entered in to the database. This drop down has been tested to ensure that it shows the categories in alphabetical order regardless of capitalisation
      of the initial letter.The `Input Word` and `Input Definition` rows have been thoroughly tested so that the functionality works and iputs a new word_id and 
      associated definition in to the database. This required a large amount of testing and with different functions and methods.
    * The `Edit Word` button submits the form to the database and overwrites the existing data. This has been extensively tested.

*	**Manage Categories Main Section**
    * The user is taken to the Categories page. The categories on this page are listed in alphabetical order regardless of the case of the initial letter. This 
      functionality required extensive testing in order make the functions work correctly.
    * The `Edit` button for each category redirects the user to the Edit Category page.  
    * The `Delete` button brings up the `Are you sure you want to delete this category??` box where the user can choose `Ok` or `Cancel`. The `Ok` button deletes the 
      category from the database completely, which functonality has been thoroughly tested. `Cancel` returns the user to the Categories page.  

*	**Edit Category Main Section**
    * The `Edit Category` button presents the user with a single row pre-populated form where the user is able to edit the `Category Name`. This will amend the 
      category_id dierctly in the database when the `Save Changes` button is pressed. This function has been extensively tested.
    * The `Cancel` button returns the user to the Browse Categories page. This has been thoroughly tested.    

*	**Add Category Main Section**
    * by pressing the `Add Category` button in the Manage Categories page the user is taken to the Add Category page, where there is a one row form. The `Category Name` 
      row allows the user to input a new category. This has been thoroughly tested so that the functionality works and iputs a new category_id in to the database. This 
      required a large amount of testing and with different functions and methods.
    * The `Add Category` button submits the form to the database and has been extensively tested.
    * The `Cancel` button returns the user to the Browse Words page. This has been thoroughly tested.

*	**Responsive / Mobile First design** 
    * Each page of the web-app has a **Header**; **Main Section** and **Footer**. These needed to display correctly accross 
      all devices and screen resolutions. primarily checks are required to ensure that the dashboard collapses in to columns in mobile view 
      and that the information is presented in a clear and legible fashion.
    * The header title was is straightened in mobile view in order to resize the Navbar sensibly. This was done to provide a 
      better user experience and clarity of design, as the title animation did not show well in a smaller view. 
    * The Side-Nav burger icon presents itself at the top-left of the NavBar in medium and small view. This has been tested across multiple 
      devices listed in this below.
    * Various methods of testing have been carried out to test the code of the web-app. Continuous testing throughout the development has been 
      implemented to check the quality of the code. The aim is to check the functionality of the code on different devices (mobile, tablet, desktop) 
      with an overall perspective of responsive and mobile first design. The site has been viewed and tested in **Firefox**, **Safari**, **Chrome** 
      **Microsoft Edge** and **Explorer**. The devices used to test the site are **iPhone 5/SE**, **Samsung Galaxy**, **iPad**, **iPad Pro** 
      **iPhone X**, **iPhone 6/7/8**, **Pixel 2**, **Pixel 2 XL** , **Hudle2** and **Samsung / Lenovo / HP laptop**. 

*	**Blank Form Input** 
    * Tested input of a blank form in all field of `input word` and `input category` (See Issues List #25)      

*	**W3 Nu Html Checker** 
    * All .html files require validation through the online checker. This ensures that the code is more legible and does 
      not contain formatting errors. https://validator.w3.org/ 

*	**W3C CSS Validator** 
    * The style.css file requires validation through the online checker. This ensures that the code is more legible and does 
      not contain formatting errors. https://jigsaw.w3.org/css-validator/validator

*	**PEP8 Online** 
    * The Python (app.py) page requires validation through the online checker. This ensures that the code is more legible and does not contain formatting 
      errors. http://pep8online.com/            
       
The final database schema and desktop wireframes for the web-app can be seen in the *supporting_docs folder* under *oceanic_dictionary_database_schema.png*, 
*wireframe1_oceanic_dictionary_home.png*, *wireframe2_ oceanic_dictionary_browse_words.png*, *wireframe3_ oceanic_dictionary_manage_categories.png* 
and unused *wireframe4_ oceanic_dictionary_manage_categories.png*. These wireframes and database schema were used initially to plan the web-app and build 
around The opinions of numerous people including my mentor, friends, tutors, chat forums and such like, whom were asked during various stages of the project.

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

The web-app is designed in the Gitpod environment and regularly committed to GitHub after each crucial piece of coding. 
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
  6. Now that your environment variables have been set in your env.py file, and the file has been imported into your project, you can use them as needed using the following syntax:  
     `MONGODB_NAME = os.environ.get('MONGODB_NAME')`

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
  12. In order for the server instance on Heroku to know how to run our Flask application, we need to specify IP and Port in Heroku. To do this go to `Settings` 
      tab > `Config Variables` and input: `IP Address: 0.0.0.0`; `Port: 5000`  

## Credits 

### Content

This README.md file is based on the Code Institute template.

### Media 

Words, Definitions and Categories in Dictionary are taken from many different sources and are mainly used as preliminary 
filling for the project. Credit to similar websites: https://digimap.edina.ac.uk/webhelp/marine/getting_started/marine_glossary.htm 
; https://life.bio.sunysb.edu/marinebio/glossary.ghijk.html ; https://www.enchantedlearning.com/wordlist/ocean.shtml ; https://www.google.com/ ; 

Homepage Paragraph: http://www.seasky.org/

Favicon image downloaded from: https://www.shutterstock.com/image-vector/dangerous-sea-life-207907852?studio=1

Favicon – created using http://www.favicomatic.com/done

Wave Image: http://www.ox.ac.uk/news/2015-12-16-freak-ocean-waves-hit-without-warning-new-research-shows

### Acknowledgments

I would like to thank all of the Code Insitute Tutors for there incredible patients and assitance and Anthony Ngene 
(https://github.com/tonymontaro) for his invaluable feedback, as supervisor for this project. 