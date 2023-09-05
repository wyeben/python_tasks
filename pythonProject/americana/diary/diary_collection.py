from americana.diary.personal_diary import PersonalDiary


class MyDiaryCollection:
    def __init__(self):
        self.diaries = []

    def add(self, diary):
        self.diaries.append(diary)

    def find_by_user_name(self, user_name):
        found_diaries = []
        for diary in self.diaries:
            if isinstance(diary, PersonalDiary):
                personal_diary = diary
                if personal_diary.get_owner() == user_name:
                    found_diaries.append(personal_diary)
        return found_diaries

    def delete(self, diary):
        self.diaries.remove(diary)
