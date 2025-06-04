# Challenge 54 - Dear Diary
from datetime import datetime

def add_entry():
    print("\nWrite your diary entry (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    if not lines:
        print("No entry written.")
        return

    entry_text = "\n".join(lines)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entry = f"\n[{timestamp}]\n{entry_text}\n" + "-"*40 + "\n"

    try:
        with open("diary.txt", "a", encoding="utf-8") as f:
            f.write(entry)
        print("Entry saved to diary.")
    except IOError as e:
        print(f"Failed to save entry: {e}")

def read_entries():
    print("\nReading Diary Entries...\n")
    try:
        with open("diary.txt", "r", encoding="utf-8") as f:
            content = f.read()
            if content.strip() == "":
                print("No entries yet.")
            else:
                print(content)
    except FileNotFoundError:
        print("No diary file found. Start by writing your first entry!")

def menu():
    while True:
        print("\nDiary Menu:")
        print("1. Write a new entry")
        print("2. View diary entries")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice in ("1", "write"):
            add_entry()
        elif choice in ("2", "view"):
            read_entries()
        elif choice in ("3", "exit"):
            print("Goodbye! Your entries are saved in 'diary.txt'")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    menu()
