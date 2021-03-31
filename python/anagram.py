from sys import argv

from mylib import WORDS_DIR, jsonData, getWords, getAnagram

def anagram(str):
    """
    The main method to get the anagram
    """
    l = len(str)
    max = jsonData['MAX_CHAR']
    min = jsonData['MIN_CHAR']
    if l > max or l < min:
        print(f"Error: please provide a word between {min} and {max}")
    else:
        words = getWords(WORDS_DIR, l)
        return getAnagram(str, words)

def main(word):
    """
    wrapper method to hold everything together
    """
    result = anagram(word)

    if result[0]:
        print(f"We found an angram for {word} > {result[0]} after {result[1]}({result[1]}) try")
    else:
        print(f"Sorry could not find anything, after {result[1]}({result[1]}) try")


if __name__ == '__main__':
    script, word = argv
    main(word)
