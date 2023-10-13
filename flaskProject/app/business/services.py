from app.data_access.diary import Diary

if __name__ == "__main__":
    username = input("Enter diary username: ")
    password = input("Enter diary password: ")
    diary = Diary(username, password)

    while True:
        print("\nDiary Menu:")
        if diary.is_locked:
            print("1. Unlock Diary")
        else:
            print("1. Lock Diary")
            print("2. Create Entry")
            print("3. Delete Entry")
            print("4. Find Entry by ID")
            print("5. Display Entries")
        print("6. Quit")

        choice = input("Select an option: ")

        if choice == '1':
            if diary.is_locked:
                password = input("Enter diary password to unlock: ")
                diary.unlock_diary1(password)
            else:
                password = input("Enter diary password to lock: ")
                diary.lock_diary()
        elif choice == '2' and not diary.is_locked:
            title = input("Enter entry title: ")
            body = input("Enter entry body: ")
            diary.create_entry(title, body)
        elif choice == '3' and not diary.is_locked:
            entry_id = int(input("Enter entry ID to delete: "))
            diary.delete_entry(entry_id)
        elif choice == '4' and not diary.is_locked:
            entry_id = int(input("Enter entry ID to find: "))
            found_entry = diary.find_entry_by_id(entry_id)
            if found_entry:
                found_entry.display()
            else:
                print(f"Entry {entry_id} not found.")
        elif choice == '5' and not diary.is_locked:
            print("\nEntries:")
            diary.display_entries()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")