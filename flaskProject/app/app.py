from flask import Flask

from app.data_access import diary
from app.data_access.diary import Diary

app = Flask(diary)


@app.route('/')
def hello_world():
    username = input("Enter diary username: ")
    password = input("Enter diary password: ")
    Diary(username, password)


if __name__ == '__main__':
    app.run()
