def create_acronym(message):
    """
    >>> print(create_acronym("random access memory"))
    RAM - random access memory
    """
    list_words = []
    while True:
        if message.find("\n") != -1:
            list_words.append(message[0:message.find("\n")])
            message = message[message.find("\n") + 1:]
        else:
            list_words.append(message)
            break
    text = ""
    for i in range(len(list_words)):
        list_of_words_in_message = list_words[i].split()
        acronym = ""

        for word in list_of_words_in_message:
            acronym += word[0]
        if i == len(list_words) - 1:
            text += acronym.upper() + " - " + list_words[i]
            break
        text += acronym.upper() + " - " + list_words[i] + "\n"

    return text

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
