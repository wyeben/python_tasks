from datetime import datetime


class Entry:
    def __init__(self, id, title, body, date_created):
        self.id = id
        self.title = title
        self.body = body
        self.date_created = date_created

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def set_body(self, body):
        self.body = body

    def get_body(self):
        return self.body

    def get_date_created(self):
        return self.date_created

    def display(self):
        print("ID:", self.id)
        print("Title:", self.title)
        print("Body:", self.body)
        print("Date Created:", self.date_created)
