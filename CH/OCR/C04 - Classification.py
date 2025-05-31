# Challenge 4 - Classification
languages = [
    ['Python',      1, 1, 0, 1, 0, 1, 0],  # interpreted, dynamically typed, not compiled, general-purpose, multi-paradigm, popular, easy syntax
    ['C',           0, 0, 1, 0, 1, 1, 0],  # compiled, statically typed, low-level, general-purpose, procedural, popular, harder syntax
    ['Java',        0, 0, 1, 0, 1, 1, 1],  # compiled (bytecode), statically typed, object-oriented, general-purpose, multi-paradigm, popular, verbose
    ['JavaScript',  1, 1, 0, 1, 0, 1, 0],  # interpreted, dynamically typed, not compiled, web, multi-paradigm, popular, easy syntax
    ['Haskell',     0, 0, 1, 0, 1, 0, 1],  # compiled, statically typed, functional, general-purpose, less popular, more complex syntax
    ['Ruby',        1, 1, 0, 1, 0, 0, 0],  # interpreted, dynamically typed, not compiled, general-purpose, multi-paradigm, less popular, easy syntax
    ['Go',          0, 0, 1, 0, 1, 1, 0],  # compiled, statically typed, general-purpose, simple syntax, popular, fast
]

questions = [
    'Is it interpreted?',               # 1
    'Is it dynamically typed?',         # 2
    'Is it compiled?',                   # 3
    'Is it used for general purpose?',  # 4
    'Is it statically typed?',           # 5
    'Is it popular?',                    # 6
    'Does it have easy syntax?'          # 7
]

print("Welcome to the programming language classifer! Answer the questions and this program will attempt to respond with a programming language that matches!")

def menu():
  while True:
    answers = []

    for question in questions:
      while True:
        answer = input(f"{question} (yes/no): ").strip().lower()
        if answer in ("yes", "no"):
          break
        else:
          print("Please answer 'yes' or 'no'.")
    
      if answer == "yes":
        answers.append(1)
      else:
        answers.append(0)

    guess = [lang for lang in languages if lang[1:] == answers]

    if guess:
      print('\nYour programming language is:', guess[0][0])
    else:
      print("\nSorry, the programming language you attempted to classify is one I do not know.")

    keep_going = input("Do you want to classify another programming language? (yes/no): ")
    if keep_going in ("no", "n"):
      print("Goodbye!")
      break

menu()
