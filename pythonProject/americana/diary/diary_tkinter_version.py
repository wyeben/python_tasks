import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime
import os


class Entry:
    def __init__(self, entry_id, title, body):
        self.entry_id = entry_id
        self.title = title
        self.body = body
        self.date_created = datetime.now()


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Diary:
    def __init__(self):
        self.username = None
        self.entries = []
        self.user_credentials = []
        self.current_user = None
        self.is_locked = True
        self.load_user_credentials()
        self.load_entries()
        self.calculate_entry_id_counter()

    def calculate_entry_id_counter(self):
        if not self.entries:
            self.entry_id_counter = 1
        else:
            self.entry_id_counter = max(entry.entry_id for entry in self.entries) + 1

    def lock_diary(self):
        self.is_locked = True

    def unlock_diary(self, password):
        if not self.is_locked:
            return
        if self.current_user and password == self.current_user.password:
            self.is_locked = False
        else:
            raise Exception("Incorrect password")

    def is_diary_locked(self):
        return self.is_locked

    def set_password(self, username, password):
        if self.is_locked:
            user = User(username, password)
            self.user_credentials.append(user)
            self.current_user = user
            self.save_user_credentials()

    def add_entry(self, entry):
        entry.entry_id = self.entry_id_counter
        self.entries.append(entry)
        self.entry_id_counter += 1
        self.save_entries()


    def delete_entry(self, entry_id):
        entry_to_delete = None
        for entry in self.entries:
            if entry.entry_id == entry_id:
                entry_to_delete = entry
                break

        if entry_to_delete:
            self.entries.remove(entry_to_delete)
            self.save_entries()
            return True
        else:
            return False

    def update_entry(self, entry_id, new_body):
        for entry in self.entries:
            if entry.entry_id == entry_id:
                entry.body = new_body
                self.save_entries()
                return True
        return False

    def find_entry_by_id(self, entry_id):
        for entry in self.entries:
            if entry.entry_id == entry_id:
                return entry

    def save_entries(self):
        if self.username:
            entries_filename = f"{self.username}_diary_entries.txt"
            with open(entries_filename, "w") as file:
                for entry in self.entries:
                    file.write(f"{entry.entry_id}\n{entry.title}\n{entry.body}\n{entry.date_created}\n")

    def load_entries(self):
        if self.username:
            entries_filename = f"{self.username}_diary_entries.txt"
            try:
                with open(entries_filename, "r") as file:
                    lines = file.read().splitlines()
                    for i in range(0, len(lines), 4):
                        entry_id = int(lines[i])
                        title = lines[i + 1]
                        body = lines[i + 2]
                        date_created = datetime.strptime(lines[i + 3], "%Y-%m-%d %H:%M:%S.%f")
                        entry = Entry(entry_id, title, body)
                        entry.date_created = date_created
                        self.entries.append(entry)
            except FileNotFoundError:
                pass

    def save_user_credentials(self):
        credentials_filename = "user_credentials.txt"
        with open(credentials_filename, "w") as file:
            for user in self.user_credentials:
                file.write(f"{user.username}\n{user.password}\n")

    def load_user_credentials(self):
        credentials_filename = "user_credentials.txt"
        try:
            with open(credentials_filename, "r") as file:
                lines = file.read().splitlines()
                for i in range(0, len(lines), 2):
                    username = lines[i]
                    password = lines[i + 1]
                    user = User(username, password)
                    self.user_credentials.append(user)
        except FileNotFoundError:
            pass


class DiaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AMERICANA DIARY APPlICATION")

        self.diary = Diary()
        self.menu_frame = tk.Frame(root)
        self.menu_frame.pack()

        self.logged_in = False

        self.login_button = tk.Button(self.menu_frame, text="Login", command=self.login)
        self.login_button.pack()

        self.create_user_button = tk.Button(self.menu_frame, text="Create User", command=self.create_user)
        self.create_user_button.pack()

        self.entry_button = tk.Button(self.menu_frame, text="Add Entry", command=self.add_entry, state=tk.DISABLED)
        self.entry_button.pack()

        self.view_button = tk.Button(self.menu_frame, text="View Entries", command=self.view_entries, state=tk.DISABLED)
        self.view_button.pack()

        self.lock_button = tk.Button(self.menu_frame, text="Lock Diary", command=self.lock_diary, state=tk.DISABLED)
        self.lock_button.pack()

        self.unlock_button = tk.Button(self.menu_frame, text="Unlock Diary", command=self.unlock_diary,
                                       state=tk.DISABLED)
        self.unlock_button.pack()

        self.update_button = tk.Button(self.menu_frame, text="Update Entry", command=self.update_entry,
                                       state=tk.DISABLED)
        self.update_button.pack()

        self.find_button = tk.Button(self.menu_frame, text="Find Entry by ID", command=self.find_entry_by_id,
                                     state=tk.DISABLED)
        self.find_button.pack()

        self.delete_button = tk.Button(self.menu_frame, text="Delete Entry", command=self.delete_entry,
                                       state=tk.DISABLED)
        self.delete_button.pack()

        self.exit_button = tk.Button(self.menu_frame, text="Exit", command=self.save_and_exit, state=tk.DISABLED)
        self.exit_button.pack()

    def login(self):
        if not self.diary.user_credentials:
            self.show_message("No users found. Create a user first.")
            return

        if self.diary.is_diary_locked():
            username = simpledialog.askstring("Login", "Enter your username:")
            if username:
                password = simpledialog.askstring("Login", "Enter your password:")
                try:
                    user = next((user for user in self.diary.user_credentials if user.username == username), None)
                    if user and user.password == password:
                        self.diary.current_user = user
                        self.diary.username = username
                        self.logged_in = True
                        self.login_button.config(state=tk.DISABLED)
                        self.create_user_button.config(state=tk.DISABLED)
                        self.entry_button.config(state=tk.NORMAL)
                        self.view_button.config(state=tk.NORMAL)
                        self.lock_button.config(state=tk.NORMAL)
                        self.unlock_button.config(state=tk.NORMAL)
                        self.update_button.config(state=tk.NORMAL)
                        self.find_button.config(state=tk.NORMAL)
                        self.delete_button.config(state=tk.NORMAL)
                        self.exit_button.config(state=tk.NORMAL)
                        self.load_entries()
                    else:
                        self.show_message("Incorrect username or password.")
                except Exception as e:
                    self.logged_in = False
                    self.show_message(str(e))
        else:
            password = simpledialog.askstring("Unlock Diary", "Enter your password:")
            try:
                if self.diary.current_user and self.diary.current_user.password == password:
                    self.diary.unlock_diary(password)
                    self.show_message("Diary unlocked.")
                    self.lock_button.config(state=tk.NORMAL)
                    self.unlock_button.config(state=tk.DISABLED)
                    self.entry_button.config(state=tk.NORMAL)
                    self.view_button.config(state=tk.NORMAL)
                    self.update_button.config(state=tk.NORMAL)
                    self.find_button.config(state=tk.NORMAL)
                    self.delete_button.config(state=tk.NORMAL)
                    self.load_entries()
                else:
                    self.show_message("Incorrect password.")
            except Exception as e:
                self.logged_in = False
                self.show_message(str(e))

    def load_entries(self):
        if self.diary.current_user:
            self.diary.entries.clear()
            self.diary.load_entries()

    def create_user(self):
        username = simpledialog.askstring("Create User", "Enter your username:")
        if username:
            password = simpledialog.askstring("Create User", "Enter your password:")
            if password:
                self.diary.set_password(username, password)
                self.show_message("User created successfully.")
                self.logged_in = True
                self.login_button.config(state=tk.DISABLED)
                self.create_user_button.config(state=tk.DISABLED)
                self.entry_button.config(state=tk.NORMAL)
                self.view_button.config(state=tk.NORMAL)
                self.lock_button.config(state=tk.NORMAL)
                self.unlock_button.config(state=tk.NORMAL)
                self.update_button.config(state=tk.NORMAL)
                self.find_button.config(state=tk.NORMAL)
                self.delete_button.config(state=tk.NORMAL)
                self.exit_button.config(state=tk.NORMAL)

    def add_entry(self):
        if self.logged_in:
            title = simpledialog.askstring("Add Entry", "Enter Entry Title:")
            if title:
                body = simpledialog.askstring("Add Entry", "Enter Entry Body:")
                if body:
                    entry = Entry(None, title, body)
                    self.diary.add_entry(entry)
                    self.show_message("Entry added successfully.")
        else:
            self.show_message("You need to be logged in to add an entry.")

    def view_entries(self):
        if self.logged_in:
            entries_text = "\n".join([f"ID: {entry.entry_id}\nTitle: {entry.title}\nBody:"
                                      f" {entry.body}\nDate Created: {entry.date_created}\n" for entry in
                                      self.diary.entries])
            if entries_text:
                self.show_message(entries_text)
            else:
                self.show_message("No entries found.")
        else:
            self.show_message("You need to be logged in to view entries.")

    def lock_diary(self):
        self.diary.lock_diary()
        self.show_message("Diary locked.")
        self.lock_button.config(state=tk.DISABLED)
        self.unlock_button.config(state=tk.NORMAL)
        self.entry_button.config(state=tk.DISABLED)
        self.view_button.config(state=tk.DISABLED)
        self.update_button.config(state=tk.DISABLED)
        self.find_button.config(state=tk.DISABLED)
        self.delete_button.config(state=tk.DISABLED)

    def unlock_diary(self):
        if self.logged_in:
            if self.diary.is_diary_locked():
                password = simpledialog.askstring("Unlock Diary", "Enter your password:")
                if password:
                    try:
                        self.diary.unlock_diary(password)
                        self.show_message("Diary unlocked.")
                        self.lock_button.config(state=tk.NORMAL)
                        self.unlock_button.config(state=tk.DISABLED)
                        self.entry_button.config(state=tk.NORMAL)
                        self.view_button.config(state=tk.NORMAL)
                        self.update_button.config(state=tk.NORMAL)
                        self.find_button.config(state=tk.NORMAL)
                        self.delete_button.config(state=tk.NORMAL)
                        self.load_entries()
                    except Exception as e:
                        self.show_message(str(e))
            else:
                self.show_message("Diary is already unlocked.")
        else:
            self.show_message("You need to be logged in to unlock the diary.")

    def delete_entry(self):
        if self.logged_in:
            entry_id = simpledialog.askinteger("Delete Entry", "Enter Entry ID to delete:")
            if entry_id:
                if self.diary.delete_entry(entry_id):
                    self.show_message(f"Entry {entry_id} deleted successfully.")
                else:
                    self.show_message(f"Entry {entry_id} not found.")
        else:
            self.show_message("You need to be logged in to delete an entry.")

    def update_entry(self):
        if self.logged_in:
            entry_id = simpledialog.askinteger("Update Entry", "Enter Entry ID to update:")
            if entry_id:
                entry = self.diary.find_entry_by_id(entry_id)
                if entry:
                    new_body = simpledialog.askstring("Update Entry", "Enter new entry body:")
                    if new_body:
                        if self.diary.update_entry(entry_id, new_body):
                            self.show_message(f"Entry {entry_id} updated successfully.")
                        else:
                            self.show_message(f"Entry {entry_id} not found.")
                else:
                    self.show_message(f"Entry {entry_id} not found.")
        else:
            self.show_message("You need to be logged in to update an entry.")

    def find_entry_by_id(self):
        if self.logged_in:
            entry_id = simpledialog.askinteger("Find Entry by ID", "Enter Entry ID to find:")
            if entry_id:
                found_entry = self.diary.find_entry_by_id(entry_id)
                if found_entry:
                    self.show_message(
                        f"ID: {found_entry.entry_id}\nTitle: {found_entry.title}\nBody:"
                        f" {found_entry.body}\nDate Created: {found_entry.date_created}")
                else:
                    self.show_message(f"Entry {entry_id} not found.")
        else:
            self.show_message("You need to be logged in to find an entry.")

    def save_and_exit(self):
        if self.logged_in:
            self.diary.save_entries()
            self.diary.save_user_credentials()
        self.root.destroy()

    def show_message(self, message):
        messagebox.showinfo("Message", message)


if __name__ == "__main__":
    root = tk.Tk()
    app = DiaryApp(root)
    root.protocol("WM_DELETE_WINDOW", app.save_and_exit)
    root.mainloop()
