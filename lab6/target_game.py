''' Target game'''
from typing import List
import random


def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    letters_list = []
    for _ in range(3):
        grid_2 = []
        for _ in range(3):
            letter = chr(random.randrange(65, 90))
            grid_2.append(letter)
        letters_list.append(grid_2)
    return letters_list

def get_words(file: str, text: List[str]) -> List[str]:
    """
    Reads the file and gets the words that are correct
    >>> get_words('en.txt', [el for el in 'wumrovkif'])
    ['fork', 'form', 'forum', 'four', 'fowk', 'from', 'frow', 'irok', 'komi', \
'kori', 'miro', 'miro', 'moki', 'ovum', 'work', 'worm', 'wouf']
    """
    new_alphabet = []
    alphabet = [chr(i) for i in range(97, 123)]
    for i in alphabet:
        if i in text:
            continue
        else:
            new_alphabet.append(i)
    try:
        with open(file) as file:
            words = []
            for line in file:
                breaking = False
                if line[0] == "#" or "Wordlists" in line:
                    continue
                line = line.lower()
                line = line.strip()
                if len(line) >= 4 and text[4] in line:
                    for alp_letter in new_alphabet:
                        if alp_letter in line:
                            breaking = True
                            break
                        for j in range(len(text)):
                            if text.count(text[j]) < line.count(text[j]):
                                breaking = True
                                break
                    if breaking:
                        continue
                    words.append(line)
    except FileNotFoundError:
        return None
    return words

def get_user_words() -> List[str]:
    """
    Gets words form user
    """
    return input().lower().split()


def get_pure_user_words(user_words: List[str], letters: List[str],\
    dictinary_words: List[str]) -> List[str]:
    """
    (list, list, list) -> list
    Checks words that are correct by rules but aren't in dictionary
    """
    user_words_fake = []
    for i in range(len(user_words)):
        if user_words[i] in dictinary_words:
            continue
        user_words_fake.append(user_words[i])

    new_alphabet = []
    alphabet = [chr(i) for i in range(97, 123)]
    for i in alphabet:
        if i in letters:
            continue
        else:
            new_alphabet.append(i)

    words = []
    for word in user_words_fake:
        breaking = False
        if len(word) >= 4 and letters[4] in word:
            for alp_letter in new_alphabet:
                if alp_letter in word:
                    breaking = True
                    break
                for j in range(len(letters)):
                    if letters.count(letters[j]) < word.count(letters[j]):
                        breaking = True
                        break
            if breaking:
                continue
            words.append(word)
    return words

def results():
    '''
    Gets the results
    '''
    letters = generate_grid()
    text = ""
    print(letters)
    for i in range(3):
        for j in range(3):
            text += letters[i][j].lower()

    correct_words = get_words("en.txt", text)
    words_entered_by_user = get_user_words()
    bad_words = get_pure_user_words(words_entered_by_user, text, correct_words)

    print(correct_words)
    print(words_entered_by_user)

    not_entered_words = correct_words
    for i in words_entered_by_user:
        if i in correct_words:
            not_entered_words.remove(i)
    correct_words_user = len(correct_words) - len(not_entered_words)
    print(not_entered_words)

    with open("result.txt", "w") as result:
        result.write(str(correct_words_user))
        result.write("\n")
        result.write(str(not_entered_words))
        result.write("\n")
        result.write(str(words_entered_by_user))
        result.write("\n")
        result.write(str(bad_words))
        result.write("\n")
        result.close()

print("lll")