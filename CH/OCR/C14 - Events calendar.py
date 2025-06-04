# Challenge 14 - Events calendar
import datetime

events = []

def is_overlapping(new_start, new_end):
    for event in events:
        existing_start = event['start']
        existing_end = event['end']
        if (new_start < existing_end and new_end > existing_start):
            return True
    return False

def add_event():
    try:
        title = input("Enter event title: ")
        start_str = input("Enter start date and time (YYYY-MM-DD HH:MM): ")
        end_str = input("Enter end date and time (YYYY-MM-DD HH:MM): ")
        start = datetime.datetime.strptime(start_str, "%Y-%m-%d %H:%M")
        end = datetime.datetime.strptime(end_str, "%Y-%m-%d %H:%M")

        if end <= start:
            print("End time must be after start time.")
            return

        if is_overlapping(start, end):
            print("Event overlaps with an existing event!")
            return

        events.append({'title': title, 'start': start, 'end': end})
        print("Event added successfully.")
    except ValueError:
        print("Invalid date/time format.")

def delete_event():
    if not events:
        print("No events to delete.")
        return

    print("List of events:")
    for i, event in enumerate(events):
        print(f"{i + 1}. {event['title']} - {event['start']} to {event['end']}")
    
    try:
        index = int(input("Enter event number to delete: ")) - 1
        if 0 <= index < len(events):
            removed_event = events.pop(index)
            print(f"Event '{removed_event['title']}' deleted.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def view_events():
    if not events:
        print("No events scheduled.")
        return
    print("\n Scheduled Events:")
    for i, event in enumerate(sorted(events, key=lambda x: x['start'])):
        print(f"{i + 1}. {event['title']} - {event['start']} to {event['end']}")

def menu():
    while True:
        print("\nCalendar Event Manager")
        print("1. Add Event")
        print("2. Delete Event")
        print("3. View Events")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip().lower()

        if choice in ('1', 'add'):
            add_event()
        elif choice in ('2', 'delete'):
            delete_event()
        elif choice in ('3', 'view'):
            view_events()
        elif choice in ('4', 'exit'):
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    menu()
