from src.notes_list import *
import datetime


def create_note():
    title = input("Enter the note title: ")
    content = input("Enter the note content: ")
    timestamp = str(datetime.datetime.now())

    notes = load_notes()
    note = {
        'id': len(notes) + 1,
        'title': title,
        'content': content,
        'timestamp': timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Note created successfully!")


def read_note():
    note_id = input("Enter the note ID: ")

    notes = load_notes()
    note = find_note_by_id(notes, note_id)
    if note:
        print_note_details(note)
    else:
        print("Note not found.")


def update_note():
    note_id = input("Enter the note ID: ")

    notes = load_notes()
    note = find_note_by_id(notes, note_id)
    if note:
        content = input("Enter the updated content: ")
        note['content'] = content
        note['timestamp'] = str(datetime.datetime.now())
        save_notes(notes)
        print("Note updated successfully!")
    else:
        print("Note not found.")


def delete_note():
    note_id = input("Enter the note ID: ")

    notes = load_notes()
    note = find_note_by_id(notes, note_id)
    if note:
        notes.remove(note)
        save_notes(notes)
        print("Note deleted successfully!")
    else:
        print("Note not found.")


def filter_notes_by_date():
    date_str = input("Enter the date (YYYY-MM-DD): ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        notes = load_notes()
        filtered_notes = [note for note in notes if datetime.datetime.strptime(note['timestamp'], "%Y-%m-%d %H:%M:%S.%f").date() == date]
        if filtered_notes:
            for note in filtered_notes:
                print_note_details(note)
                print()
        else:
            print("No notes found for the given date.")
    except ValueError:
        print("Invalid date format. Please enter a date in the format YYYY-MM-DD.")



def find_note_by_id(notes, note_id):
    for note in notes:
        if str(note['id']) == note_id:
            return note
    return None


def print_note_details(note):
    print(f"ID: {note['id']}")
    print(f"Title: {note['title']}")
    print(f"Content: {note['content']}")
    print(f"Last edit date: {note['timestamp']}")


def print_all_notes():
    notes = load_notes()
    if len(notes) > 0:
        for note in notes:
            print_note_details(note)
            print()
    else:
        print("No notes found.")
