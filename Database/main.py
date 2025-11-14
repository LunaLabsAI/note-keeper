import sqlite3

conn = sqlite3.connect("notes.db")
cursor = conn.cursor()

def menu():
    print("\n--- Simple Note Keeper ---")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Search Notes")
    print("4. Delete Note")
    print("5. Exit")
    return input("Choose an option: ")

def main():
    create_db()
    while True:
        choice = menu()
        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            add_note(title, content)
        elif choice == "2":
            for note in view_notes():
                print(note)
        elif choice == "3":
            keyword = input("Search keyword: ")
            results = search_notes(keyword)
            for r in results:
                print(r)
        elif choice == "4":
            note_id = input("Enter note ID to delete: ")
            delete_note(note_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
