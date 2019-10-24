## Python Flask Experimentation

#### Experiment and learn Python, Flask, SQLAlchemy, and more

To clone the remote repository

```text
git clone https://github.com/jkmalan/jkm-journal.git
```

To prepare the development environment, including dependencies, from the root directory

```text
pip install pipenv   # Please install pipenv, don't use pip! Requires root privileges

pipenv install

pipenv shell
```

To run the project and auto-generate the database, from the root directory

```text
export FLASK_APP=app.py

flask run
```

To be able to use IBM Watson processing features, include a WATSON_SECRET environment variable

```text
export WATSON_SECRET=<insert your secret key>
```