# Here is the full list of challenges in the OCR coding challenges booklet. The tick marks show the ones I have completed.
# Ones with a hashtag are ones I am unlikely to complete (for now).

items = [
    ("C01", "Factorial Finder", "✅"),
    ("C02", "Speed Tracker", "✅"),
    ("C03", "Thief", "✅"),
    ("C04", "Classification", "✅"),
    ("C05", "Fruit Machine", "✅"),
    ("C06", "Unit Converter (temperature, currency, volume)", "✅"),
    ("C07", "Credit Card Validator", "✅"),
    ("C08", "Arithmetic test", "✅"),
    ("C09", "Happy Numbers", "✅"),
    ("C10", "Number Names", "✅"),
    ("C11", "Regex Query Tool", "✅"),
    ("C12", "Quiz Maker", "✅"),
    ("C13", "Caesar Cipher", "✅"),
    ("C14", "Events calendar", "✅"),
    ("C15", "Pangrams", "✅"),
    ("C16", "Kaprekar", "✅"),
    ("C17", "Number Table", "✅"),
    ("C18", "Years in a Range", "✅"),
    ("C19", "Logic Gate", "✅"),
    ("C20", "Palindromes", "✅"),
    ("C21", "Data Entry", "✅"),
    ("C22", "Simple Life Calculator", "✅"),
    ("C23", "Fibbing", "✅"),
    ("C24", "Hack-proof", "✅"),
    ("C25", "Ordering", "✅"),
    ("C26", "Truth or not!", "❌"),
    ("C27", "Word Subtraction", "✅"),
    ("C28", "Name that Number", "❌"),
    ("C29", "Item Merge", "✅"),
    ("C30", "Year Addition", "✅"),
    ("C31", "Forwards and Backwards", "✅"),
    ("C32", "Code it up", "✅"),
    ("C33", "Mor-se Coding", "✅"),
    ("C34", "What's the day?", "✅"),
    ("C35", "Game of Chance", "✅"),
    ("C36", "Triangulate", "✅"),
    ("C37", "Fizz Buzz", "✅"),
    ("C38", "Sing Along", "✅"),
    ("C39", "Even more Odd", "✅"),
    ("C40", "Base of Numbers", "✅"),
    ("C41", "Prime Factorisation", "✅"),
    ("C42", "Tilers mate", "✅"),
    ("C43", "The meaning of life", "❌"), #
    ("C44", "Sudoku", "❌"), #
    ("C45", "Find the factorial", "✅"),
    ("C46", "Complex Numbers", "❌"),
    ("C47", "Happy Numbers =)", "✅"),
    ("C48", "Reverse it", "✅"),
    ("C49", "Fireworks", "❌"), #
    ("C50", "Mandelbrot Set", "❌"), #
    ("C51", "Text-speak converter", "✅"),
    ("C52", "Is this card valid?", "✅"),
    ("C53", "Mortgage Calculator", "✅"),
    ("C54", "Dear Diary", "✅"),
    ("C55", "Secret Ciphers", "✅"),
    ("C56", "Page Scraper", "❌"), #
    ("C57", "Such meme, many like", "❌"), #
    ("C58", "Text based game", "✅"),
    ("C59", "CSV File Utility", "❌"), #
    ("C60", "Get GIFy with it", "❌"), #
    ("C61", "Your name is…", "✅"),
    ("C62", "R@nd0m P@ssw0rd generator", "✅"),
    ("C63", "I like Pi", "✅"),
    ("C64", "Galaxy song", "❌"), #
    ("C65", "Spam filter", "✅"),
    ("C66", "Silly walks", "❌"), #
    ("C67", "What have the Romans ever done for us?", "✅"),
    ("C68", "Semaphore", "❌"), #
    ("C69", "Beautiful soup", "❌"), #
    ("C70", "Of mice and men", "✅"),
    ("C71", "Goldbach", "✅"),
    ("C72", "Lists", "✅"),
    ("C73", "Travel club", "❌"),
    ("C74", "Checkmate checker", "❌"), #
    ("C75", "String permutation", "✅"),
    ("C76", "That's a lot of number", "✅"),
    ("C77", "Fib on a chi", "✅"),
    ("C78", "2 fiddy", "✅"),
    ("C79", "Printer problems", "❌"), #
    ("C80", "Happy Hopper", "✅"),
]

max_title_len = max(len(f"{code} - {title}") for code, title, status in items)

for code, title, status in items:
    line = f"{code} - {title}"
    print(f"{line.ljust(max_title_len)}   {status}")
