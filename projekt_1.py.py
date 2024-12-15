"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Petr Vrba

email: pvrba01@gmail.com

discord: petrv_95056
"""


import string

TEXTS = [
    """Situated about 10 miles west of Kemmerer, 
    Fossil Butte is a ruggedly impressive topographic feature that rises 
    sharply some 1000 feet above Twin Creek Valley to an elevation of more 
    than 7500 feet above sea level. The butte is located just north of US 30N and the Union Pacific Railroad,
    which traverse the valley.""",

    """At the base of Fossil Butte are the bright red, purple, yellow and gray 
    beds of the Wasatch Formation. Eroded portions of these horizontal beds 
    slope gradually upward from the valley floor and steepen abruptlyOverlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick..""",

    """The monument contains 8198 acres and protects a portion of the largest 
    deposit of freshwater fish fossils in the world. The richest fossil fish 
    deposits are found in multiple limestone layers, which lie some 100 feet 
    below the top of the butte The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present."""
]

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

def authenticate_user():
    username = input("Zadejte přihlašovací jméno: ")
    password = input("Zadejte heslo: ")

    if username in users and users[username] == password:
        print(f"Vítejte, {username}!")
        return True
    else:
        print("Invalid name or password, the program is terminating.")
        return False

def select_text():
    print("\nWe have 3 texts to analyze.")
    while True:
        try:
            choice = int(input("Enter a number btw. 1 and 3 to select one text: "))
            if 1 <= choice <= len(TEXTS):
                return TEXTS[choice - 1]
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

def remove_punctuation(word):
    return word.strip(string.punctuation)

def analyze_text(text):
    words = [remove_punctuation(word) for word in text.split()]
    word_count = len(words)
    titlecase_count = sum(1 for word in words if word.istitle())
    uppercase_count = sum(1 for word in words if word.isupper() and word.isalpha())
    lowercase_count = sum(1 for word in words if word.islower())
    numeric_count = sum(1 for word in words if word.isdigit())
    numeric_sum = sum(int(word) for word in words if word.isdigit())

    print("\n==== TEXT ANALYSIS ====")
    print(f"There are {word_count} words in the selected text.")
    print(f"There are {titlecase_count} titlecase words.")
    print(f"There are {uppercase_count} uppercase words.")
    print(f"There are {lowercase_count} lowercase words.")
    print(f"There are {numeric_count} numeric strings.")
    print(f"The sum of all the numbers {numeric_sum}")

    word_lengths = [len(word) for word in words]
    length_freq = {length: word_lengths.count(length) for length in set(word_lengths)}

    print("-" * 40)
    print(f"{'LEN':<3}| {'OCCURENCES':<12}|NR.")
    print("-" * 40)
    for length, freq in sorted(length_freq.items()):
        print(f"{length:<3}|{'*' * freq:<12}|{freq}")

if __name__ == "__main__":
    if authenticate_user():
        selected_text = select_text()
        if selected_text:
            analyze_text(selected_text)
