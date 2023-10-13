import os
from datetime import datetime

from app.data_access.entry import Entry

DIARY_DIRECTORY = "diary_entries"
os.makedirs(DIARY_DIRECTORY, exist_ok=True)


class Diary:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_locked = True
        self.entries = []
        self.entry_id_counter = 1
        self.load_entries()

    def lock_diary1(self):
        self.is_locked = True
        print("Diary locked.")

    def unlock_diary1(self, password):
        if self.is_locked:
            if password == self.password:
                self.is_locked = False
                print("Diary unlocked.")
            else:
                print("Incorrect password. Diary remains locked.")
        else:
            print("Diary is already unlocked.")

    def create_entry(self, title, body):
        if not self.is_locked:
            entry = Entry(self.entry_id_counter, title, body, datetime.now())
            self.entries.append(entry)
            self.entry_id_counter += 1
            self.save_entries()
            print("Entry created successfully!")
        else:
            print("Diary is locked. Cannot create entry.")

    def delete_entry1(self, entry_id):
        if not self.is_locked:
            self.entries = [entry for entry in self.entries if entry.id != entry_id]
            self.save_entries()
            print(f"Entry {entry_id} deleted.")
        else:
            print("Diary is locked. Cannot delete entry.")

    def find_entry_by_id1(self, entry_id):
        for entry in self.entries:
            if entry.id == entry_id:
                return entry
        return None

    def display_entries(self):
        if not self.entries:
            print("No entries to display.")
        else:
            for entry in self.entries:
                entry.display()

    def load_entries(self):
        file_path = os.path.join(DIARY_DIRECTORY, f"{self.username}_diary.txt")
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split("|")
                    if len(parts) == 4:
                        entry = Entry(int(parts[0]), parts[1], parts[2], datetime.fromisoformat(parts[3]))
                        self.entries.append(entry)

    def save_entries1(self):
        file_path = os.path.join(DIARY_DIRECTORY, f"{self.username}_diary.txt")
        with open(file_path, "w") as file:
            for entry in self.entries:
                file.write(f"{entry.id}|{entry.title}|{entry.body}|{entry.date_created.isoformat()}\n")
