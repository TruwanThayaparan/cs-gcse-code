# Challenge 11 - Regex Query Tool
import re

while True:
    try:
        user_text = input("\nEnter the text to search: ")
        pattern = input("Enter the regex pattern: ")
        
        p = re.compile(pattern)
        matches = p.findall(user_text)

        if matches:
            print("Matches found:")
            for match in matches:
                print(f"- {match}")
        else:
            print("No matches found.")

    except re.error as e:
        print(f"Regex error: {e}")

    except KeyboardInterrupt:
        print("Exiting. Goodbye!")
        break

    again = input("Want to try again? (yes/no): ").strip().lower()
    if again in ("no", "n"):
        print("Goodbye!")
        break
