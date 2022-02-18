# Description

This repository is the backend for the Expense Tracker.  It handles any user authentication, sign up, log in, and data retrieval and edits.  If you would like to visit the application please visit the frontend repository listed below.

GitHub Repository: https://github.com/leejoonli/expense-tracker

It is strongly recommended you follow the GitHub respository guide to view/use the application.

## API Routes

### API Root
https://salty-eyrie-01871.herokuapp.com/

### API Route Paths

| Method | Route | Description |
| ------ | ----- | ----------- |
| GET | /expenses/ | Read all expenses by user |
| GET | /expenses/:id | Read one expense by user |
| POST | /expenses/ | Create an expense |
| PUT | /expenses/:id | Update an expense |
| DELETE | /expenses/:id | Delete an expense |

\* Note: User must be logged in to complete routes as this application uses user authentication.

## Technologies Used

- Python v3.8
- Django
- Django Rest Framework
- Psycopg2-binary
- Dj-database-url
- Gunicorn
- Djoser
- Django-cors-headers
- Whitenoise
- Django-filter
- Heroku

## Installation

1. Open your terminal and navigate to your desire directory where you want to store this repository using `cd <YOUR DIRECTORY HERE>`
2. On the GitHub repository, click on the "Code" dropdown menu and either click on "HTTPS" or "SSH" depending on what you're using.
3. You can either click the link which will highlight the GitHub or https link and copy it or click on the icon next to the link which will copy it into your clipboard.
4. Fork and clone this repository to your machine using `git clone <PASTE SSH OR HTTPS HERE>`
5. `cd` into the newly created directory
6. Run `npm i` or `npm install` to install dependencies

### Locally Run Backend

1. To run the backend locally, you will need to install PostgreSQL.  Follow the link below for installation.
2. Then check to see if you're PostgreSQL is online by running `service postgresql status`
3. If the database is not online run `service postgresql start`.  If you're using WSL run `sudo service postgresql start`.
4. Then run `pipenv shell`
5. In the shell, run `python3 manage.py runserver`
6. To open in code editor, use `code .`

\* Note: You will not have any data if you run locally since you haven't posted any data.  It is recommended you don't run things locally and use the database hosted by Heroku and use the endpoints provided above.

## Future Improvments

- More data to the expense model.
- Add search functionality.
- Add pagination functionality.

## Contribution Guidelines

### How to Identify Bugs

> If you identify bugs, submit an issue on the Git repo. Please detail the bug in your issue. If you know how to fix it, feel free to note the methods you would use. You could also submit a pull request with suggested code to fix it.

## Initial Planning

## List of Technologies
Backend: Django, Python, SQL, AWS

### List of backend models and their properties
```python
class Expense
    name
    amount
    category
    date
    owner

class User
    email
    avatar
```

## Unsolved Problems

No query parameter functionality is currently implemented.  And I can forsee problems with pagination once a user's amount of data gets large enough.  Hopefully, adding more detail to the expense tracker model won't have any migration problems.

## Major Hurdles

The biggest hurdle regarding the backend would be using the Django Rest Framework.  There's so much involved when it comes to the Django Rest Framework that it felt overwhelming at times, but I was also very interested in what else the package provides.  The next step would be to add query parameters and possibly add pagination depending on the amount of data.  Thankfully, the markdowns provided were very well documented and I was able to follow step by step to create the database with Django and PostgreSQL.