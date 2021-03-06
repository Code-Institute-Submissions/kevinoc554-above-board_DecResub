# Testing

The following describes the testing steps taken during the development of [Above Board](http://above-board.herokuapp.com/).

Full details ofthe site can be found in the [README](README.md).

# Table of Contents
> 1.  [Validators](#validation)
> 2.  [User Stories](#user-stories)
> 3.  [Manual Testing](#manual-testing)
> 4.  [Automated Testing](#automated-testing)
> 5.  [Bugs](#bugs)

# Validation:

### HTML

- The HTML for the site's four pages was passed through the W3C Markup Validation Service.
- The validator flagged `Bad value true for attribute readonly on element input`, however this was unavoidable due to how Materialize handles select elements.

### CSS

- The site's CSS was passed through the W3C CSS Validation Service, and no errors were found.
- The validation tool highlighted some vendor prefixes which were added by [Autoprefixer](http://autoprefixer.github.io/) to ensure cross-browser support.

### JS

- The site's JavaScript was validated using JSHint.

### Python

- The Python code was written in an attempt to comply with PEP-8 standards, with the following exceptions:
    - games/forms.py - error: line too long: The variable in question is a URL, and was left intact to ensure readability.
    - games/utils.py - warning: possible unbalanced tuple - The implementation of pagination (based on [this](https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9) guide) requires the tuple to be unbalanced to function.
    - aboveboard/config.py - warning: 'env' imported but unused: This is used solely to set environment variables locally,isnot pushed to githud/heroku.

# User Stories
1. As a new user, I want to be able to register an account, so I can fully utilize the site.
    - New users can access the Register page via the large call to action button featured prominently on the Home page, or via the Register link in the navigation bar of every page.
2. As a returning user, I want to be able to log in easily, so I can access the site’s features.
    - The site's login page is accessible at all times via the navigation bar.
    - Additionally, shouldthe user attempt to access aroute or page that they do not have permission to access without logging in, they will be redirected to the login page. The login route will then direct them back to the page they were originally trying to access.
3. As a boardgame fan, I want to be able to view, search and filter a database of games, so I can find one to play.
    - Users can access the All Games page, which displays the entire database of games, sorted alphabetically and paginated to show 8 results per page.
    - Users can browse through the games to see details like the genre, player count and an average of all the users ratings.
    - Users can utilize the text indexed search to filter through the games.
    - Users can use this information to make an informed decision when picking a game to play or buy. 
4. As a boardgame fan, I want to add my games to the database, so I can curate my collection.
    - Users can access the Add Game page via the button on the Home, Profile, All & My Games pages.
    - Users can add a range of data about the game, including a brief description and a link to the box art.
5. As a boardgame fan, I want to view my collection of games to the database, so I can see all the games I have added.
    - Once users have added a game, this can be viewed on the user's My Games page.
    - This page has the same functionality as the All Games page but only displays games that the current user has added.
6. As a boardgame fan, I want rate games in the database, so I can provide guidance to other users.
    - Any logged in user can rate any game in the database by clicking into it's individual page and using the intuitive star rating system.
7. As a site user, I want to be able to delete my posts, so I can remove any games I have posted.
    - Users can delete and edit any games they have added to the database via the labelled buttons on that game's page.
8. As a site administrator, I want to be able to delete any user’s games, so I can remove any potentially inappropriate content.
    - The Admin account can delete and edit any game added to the database.
9. As a site administrator, I want to be able to add new genres and mechanics, so I can expand the database content in line with user demands.
    - The Admin can access an admin page where they can add new Genres or MEchanics to the database.
    - Once added these will appear in the dropdown menus on the Add and Edit Game pages for all users.

# Manual Testing

## Testing Environments

Development and initial testing took place on a HP 250 G6 Laptop (Windows 10) in Chrome. Subsequent testing took place across the following devices, operating systems and browsers:

- Devices:

  - HP 250 G6 Laptop (Windows 10)
  - MacBook Pro 2013 (MacOS)
  - OnePlus 6T (Oxygen OS)
  - Samsung Galaxy S9 (Android)
  - Apple iPad (iPadOS 14)
- Browsers:

  - Chrome
  - Firefox
  - Edge
  - Safari

*All testing steps were taken on all devices and browsers, unless otherwise stated.*

## Responsive Testing
- All pages of the site were manually tested on a variety of browsers and devices to ensure the design is legible and useable at all screen sizes.

## CRUD Functionality
The CRUD (Create, Read, Update and Delete) functionality of the site was manually tested.

### **Create**
|Functionality|Expected|Outcome|
---|---|---
|Register a user account|User found in database|Pass|
|Add a game|Game found in database, and visible on the site|Pass|
|Add a genre or mechanic via Admin page|Genre/Mechanics found in database, and visible on the site|Pass|


### **Read**
|Functionality|Expected|Outcome|
---|---|---
|View a user's account details from database|Account info visible on Profile page|Pass|
|View games from database|Game visible on the Home, All & My Games pages|Pass|
|View genre and mechanics from database|Genre/Mechanics visible in forms on the Add and Edit Game pages|Pass|


### **Update**
|Functionality|Expected|Outcome|
---|---|---
|Update a user's account details|New account info visible in database and on Profile page|Pass|
|Update game data|New game data visible in database and on the site|Pass|


### **Delete**
|Functionality|Expected|Outcome|
---|---|---
|Delete a game|Game no longer visible in database or on the site|Pass|


# Automated Testing
Unit tests for some of the site's features and routes were implemented in `test.py`.

These tests were built using the `unittest` and `flask-testing` packages. These packages are included on requirements.txt.

At the time of submission, all tests are passing:

![Screenshot of test results](screenshots/tests.PNG)

Test GET Routes:

A Test Case was built to test GET requests to various routes by a user that has not logged in. A selection of tests will be displayed below, and the full test suite can be found in `test.py`.

1. test_home & test_home_variant
    - Expected:
        - Status 200
    - Result: 
        - Pass

2. test_all_games
    - Expected: 
        - Status 200
        - 'pagination-page-info'- if present, pagination has applied
    - Result:
        - Pass

3. test_profile
    - Expected: 
        - Status 302 - redirect as login is required
    - Result:
        - Pass

4. test_my_games
    - Expected: 
        - Status 302 - redirect as login is required
    - Result:
        - Pass


Test POST Routes:

A Test Case was built to test POST requests to various routes, and GET requests with a logged in user. These tests use dummy data to register a user, log that user in and out, update their account details and add a game to the database. The TestCase's class method then automatically deletes the user and game from the database at the end of testing. The tests are named with letter characters near the start of the test name to ensure they fire in the correct order. A selection of tests will be displayed below, and the full test suite can be found in `test.py`.

1. test_a_register_user
    - Expected: 
        - Status 302 - redirects to Home on success
        - New user found in database
    - Result:
        - Pass

2. test_b_login_user
    - Expected: 
        - Status 302 - redirects to Home on success
        - Once logged in current_user.username should be 'unittest'
    - Result:
        - Pass

3. test_c_add_game
    - Expected: 
        - Status 302 - redirects to All Games on success
        - New game found in database
    - Result:
        - Pass

4. test_my_games_logged_in
    - Expected: 
        - Status 200
        - 'pagination-page-info'- if present, pagination has applied
    - Result:
        - Pass

5. test_zlogout_user
    - Expected: 
        - Status 302
        - As user is logged out, current_user.is_authenticated is False
    - Result:
        - Pass

# Bugs

## Fixed
**Login not working:**

Issue: 
- Login user method does not throw an error, redirects to homepage and creates a session cookie as intended, but the current_user.is_authenticated still comes back as false.
- When printing current_user after leaving the original route, get `flask_login.mixins.AnonymousUserMixin`
- Judicious use of print statements showed the load_user function was passing in the email address correctly, but then returning None rather than the User object.
- Investigation highlighted a typo in load_user, “mongo.db.User” vs. “mongo.db.users”.

Fix:
- Typo has been corrected and login now functions correctly.

**Login route fails with a 500 error if email provided is not in the database**

Issue:
- Login route was failing if the email provided was not in the database.
- The function to check the password hash was expecting a result fromthe find_user method, and was causing an error if find_user returned None.

Fix:
- The check passwrod has function is now wrapped in an if statement,and only fires if the find_user method returns a result (i.e., is not None). If not, the Login page will be refeshed and a flashed message displayed.

**View Game route crashing if given an invalid/wrong length game id:**

Issue:
- The View Games route was unable to handle being passed an invalid game id, and was causing 500 errors.
- An invalid id could be one that is manually inputted by a user and could be the wrong length or could point to a game that is no longer in the database.

Fix:
- Wrapped the route in a try/except block. In the event the route fails, will redirect the user to the All Games route and flash a message to explain rather than throwing an error.

**An error displaying in the console for the star ratings JavaScript function, only on pages where it is unused.**

Issue:
- The function gets the average rating from a div with the id of 'rating-avg'.
- On pages where this div did not exist, the function would fail with a syntax error.

Fix:
- Wrapped the function in an if statement, so it only fires on pages where the '#ratings-avg' div exists.

## Remaining
- At the time of submission, no outstanding bugs were identified.