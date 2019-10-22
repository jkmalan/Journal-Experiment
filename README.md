## Python Flask Experimentation

#### Experiment and learn Python, Flask, SQLAlchemy, and more

To clone the remote repository

```text
git clone https://github.com/jkmalan/jkm-journal.git
```

To prepare the development environment, including dependencies, from the root directory

```text
pip install pipenv   # Necessary if not already installed, requires root privileges

pipenv install

pipenv shell
```

To run the project and auto-generate the database, from the root directory

```text
export FLASK_APP=app.py

flask run
```