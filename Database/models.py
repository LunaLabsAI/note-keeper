import sqlite3

DB = "notes.db"

def add_note(title, content):
    with sqlite3.connect(DB) as conn:
        conn.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
        conn.commit()

def view_notes():
    with sqlite3.connect(DB) as conn:
        cursor = conn.execute("SELECT id, title, content, created_at FROM notes")
        return cursor.fetchall()

def search_notes(keyword):
    with sqlite3.connect(DB) as conn:
        cursor = conn.execute("SELECT * FROM notes WHERE title LIKE ? OR content LIKE ?", 
                              (f"%{keyword}%", f"%{keyword}%"))
        return cursor.fetchall()

def delete_note(note_id):
    with sqlite3.connect(DB) as conn:
        conn.execute("DELETE FROM notes WHERE id=?", (note_id,))
        conn.commit()
