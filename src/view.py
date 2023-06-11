from src.command import *


def start_command_window():
    print("\nHowdy, mate! Feel free to pick a command number: ")
    while True:
        print("Choose the command:")
        print("1. Create a note")
        print("2. Read a note")
        print("3. Update a note")
        print("4. Delete a note")
        print("5. List all notes")
        print("6. Filter notes by date")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")
        print()

        if choice == '1':
            create_note()
        elif choice == '2':
            read_note()
        elif choice == '3':
            update_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            print_all_notes()
        elif choice == '6':
            filter_notes_by_date()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")
