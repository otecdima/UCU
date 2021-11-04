'''Lab 6.9'''
import random

def generate_grid():
    '''
    Random grid
    '''
    random_letters = []
    alphabet_ua = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    alphabet_ua = list(alphabet_ua)
    while len(random_letters) < 5:
        letter = random.choice(alphabet_ua)
        if letter not in random_letters:
            random_letters.append(letter)
    return random_letters

def get_words(link_file, letters):
    '''
    Checks words from file
    >>> get_words("base.lst", ['ю', 'щ', 'я', 'ц', 'г']) #doctest: +ELLIPSIS
    [('габа', 'noun'), ('габро', 'noun'), ('гавин', 'adjective')...
    '''
    final_list = []
    with open(link_file) as file:
        for line in file:
            line.strip()
            line.encode('utf-8')
            index = line.find(" ")
            word, things = line[0:index], line[index:]
            things = things.lstrip()
            if len(word) > 5 or len(word) < 1:
                continue
            for i in letters:
                if i == word[0]:
                    break
            else:
                continue
            if "noninfl" in things or "intj" in things:
                continue

            if things.startswith("adv") or things.startswith("/adv"):
                final_list.append((word, "adverb"))
            elif things.startswith("adj") or things.startswith("/adj"):
                final_list.append((word, "adjective"))
            elif "/n" in things or "noun" in things:
                final_list.append((word, "noun"))
            elif "/v" in things:
                final_list.append((word, "verb"))
    return final_list

def check_user_words(user_words, language, text, dictionary_words):
    """
    Checks whether the words entered by user are correct
    >>> check_user_words(['гаяти', 'гнати', 'ініціалізація', 'узяти', 'щавель'], "verb",\
['ю', 'щ', 'я', 'ц', 'г'], get_words("base.lst", ['ю', 'щ', 'я', 'ц', 'г']))
    (['гаяти', 'гнати'], ['гнити', 'гнути', 'гоїти', 'грати', 'гріти', 'густи', \
'юшити', 'явити', 'яріти', 'ячати'])
    """
    right_entered_words = []
    untyped_words = []
    for i in range(len(user_words)):
        if user_words[i][0] not in text or len(user_words[i]) > 5:
            right_entered_words.append(user_words[i])

    correct_guessed_words = []

    for i in dictionary_words:
        if i[0] not in user_words:
            if i[1] == language:
                untyped_words.append(i[0])
        elif i[0] in user_words:
            if i[1] == language:
                correct_guessed_words.append(i[0])
    return correct_guessed_words, untyped_words

def get_user_words():
    """
    Input that gets words from a user
    """
    return input().lower().split()

def language_part_gen():
    """
    Generates a random language part
    """
    language = ['noun', 'verb', 'adjective', 'adverb']
    return random.choice(language)
