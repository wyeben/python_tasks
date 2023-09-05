import unittest
from datetime import datetime

from americana.diary_with_colors import Diary, User, Entry


class TestDiary(unittest.TestCase):
    def setUp(self):

        self.diary = Diary()
        self.user = User("Benson", "password")
        self.diary.user_credentials.append(self.user)
        self.diary.current_user = self.user
        self.diary.username = "Benson"

    def test_add_entry(self):
        entry = Entry(None, "Today", "Today is a good day.")
        self.diary.add_entry(entry)
        self.assertEqual(len(self.diary.entries), 1)

    def test_delete_entry(self):
        entry = Entry(None, "Today", "Today is a good day.")
        self.diary.add_entry(entry)
        entry_id = entry.entry_id
        result = self.diary.delete_entry(entry_id)
        self.assertTrue(result)
        self.assertEqual(len(self.diary.entries), 0)

    def test_update_entry(self):
        entry = Entry(None, "Today", "Today is a good day.")
        self.diary.add_entry(entry)
        entry_id = entry.entry_id
        new_body = "Updated entry."
        result = self.diary.update_entry(entry_id, new_body)
        self.assertTrue(result)
        updated_entry = self.diary.find_entry_by_id(entry_id)
        self.assertEqual(updated_entry.body, new_body)

    def test_find_entry_by_id(self):
        entry = Entry(None, "Today", "Today is a good day.")
        self.diary.add_entry(entry)
        entry_id = entry.entry_id
        found_entry = self.diary.find_entry_by_id(entry_id)
        self.assertEqual(found_entry.entry_id, entry_id)

    def test_lock_diary(self):
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_diary_locked())

    def test_unlock_diary(self):
        self.diary.unlock_diary("password")
        self.assertFalse(self.diary.is_diary_locked())

if __name__ == "__main__":
    unittest.main()
