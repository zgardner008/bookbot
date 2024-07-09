total_word_count = 0
character_count = {}

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_total = word_count(file_contents)

    print(f"There are {word_total} words.")

def word_count(text):
    words = text.split()
    for word in range(len(words)):
        total_word_count = len(words) 

    return total_word_count

main()
