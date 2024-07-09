total_word_count = 0
character_count = {}
character_split = []
char_stats = {}
sorted = []

def main():
    with open("books/frankenstein.txt") as book:
        file_contents = book.read()

    word_total = word_count(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_total} words found in the document.")
    print()
    num_char = char_counter(file_contents)
    sorted_char = sort_char(num_char)

    for stat in sorted_char:
        for entry in stat:
            print(f"The {entry} character was found {stat[entry]} times.")

def char_counter(text_string):
    lowered_text_string = text_string.lower()
    character_split = [*lowered_text_string]
    for char in character_split:
        if char.isalpha():
            if char not in char_stats:
                char_stats[char] = 1
            else:
                char_stats[char] += 1
    return char_stats

def word_count(text):
    words = text.split()
    total_word_count = len(words)

    return total_word_count

def sort_char(unsorted):
    for char_dict in unsorted:
        sort_dict = {}
        sort_dict[char_dict] = unsorted[char_dict]
        sorted.append(sort_dict)
    sorted.sort(reverse=True, key=sort_on)

    return sorted

def sort_on(occurances):
    for i in occurances:
        return occurances[i]

main()
