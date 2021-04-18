# Udemy-Flask

Learning to develop websites using Python Flask, Bootstrap, CSS/HTML. Ideally this course will help me to understand how to develop the ultimate portfolio website.


## Setting Flask App

Before running a flask app, you need to pass the application file to the local flask package in your current environment. The most common application names are `application`/`app` and `model`. Export the app name to flask like so:

```BASH
export FLASK_APP=application.py
```


## Initializing Database

Flask requires that the underlying database be initialized. The initialization process will create a migrations folder in the local application's home directory. From this migrations folder, the changes must be committed and executed like so:

```BASH
flask db init
flask db migrate -m "... message"
flask db upgrade
```



*Alice Seaborn. c. 2020.*
