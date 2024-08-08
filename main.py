def main():
    book_path = 'books/frankenstein.txt'
    the_book = get_book(book_path)
    amount_words = count_words(the_book)
    total_characters = count_characters(the_book)
    dicionary_sorted = sort_dict(total_characters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{amount_words} words were found in the document\n")
    for key in dicionary_sorted:
        if key.isalpha():
            print(f"The '{key}' character was found {total_characters[key]} times.")
    print(f"--- End Report ---")

def count_words(book):
    words = book.split()
    return len(words)

def get_book(path):
    with open(path) as f:
        return f.read()

def count_characters(book):
    letter_dictionary = {}     
    
    for c in book:
        lowered = c.lower()
        if lowered in letter_dictionary:
            letter_dictionary[lowered] += 1
        else:
            letter_dictionary[lowered] = 1

    return letter_dictionary

def sort_dict(dictionary):
    sorted_dict = dict(sorted(dictionary.items()))
    return sorted_dict

main()
