import json


def load_notes():
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes


def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)
