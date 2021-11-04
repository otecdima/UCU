def dyvo_insert(sentence, flag):
    """
    Inserting word "диво" before every word that starts with flag.
    >>> dyvo_insert("кит", "ки")
    диво кит
    >>> dyvo_insert("Кит кота по хвилях катав - кит у воді, кіт на киті.", "ки")
    """
    # index = sentence.find(flag)
    # final_string = sentence[:index] + 'диво ' + sentence[index:]
    # return print(final_string)

    # str = "thisissometextthatiwrotetext"
    substr = flag
    sentence = sentence.lower()
    inserttxt = "диво"
    new_string = (inserttxt+substr).join(sentence.split(substr))
    return print(new_string)

dyvo_insert("кит", "ки")
dyvo_insert("Кит кота по хвилях катав - кит у воді, кіт на киті.", "ки")
    