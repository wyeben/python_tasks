from americana.diary.diary import Diary


class PersonalDiary(Diary):
    def __init__(self, username, password, owner):
        super().__init__(username, password)
        self.owner = owner

    def get_owner(self):
        return self.owner

    def create_entry(self, title, body):
        super().create_entry(title, body)

    def display_entries(self):
        print(f"Personal Diary for {self.owner}")
        super().display_entries()
