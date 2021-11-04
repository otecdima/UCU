def caesar_encode(message, key):
    """
    >>> caesar_encode("hello world", 2)
    'jgnnq yqtnf'
    """
    encrypted = ""
    message = message.lower()
    for letter in message:
        if letter != " ":
            new_index = (ord(letter) - ord("a") + key) % 26
            newcodeofletter = new_index + ord("a")
            encrypted = encrypted + chr(newcodeofletter)
        else:
            encrypted = encrypted + letter
    return encrypted

def caesar_decode(message, key):
    """
    >>> caesar_decode("jgnnq yqtnf", 2)
    'hello world'
    """
    decrypted = ""
    message = message.lower()
    for letter in message:
        if letter != " ":
            new_index = (ord(letter) - ord("a") - key) % 26
            newcodeofletter = new_index + ord("a")
            decrypted += chr(newcodeofletter)
        else:
            decrypted = decrypted + letter
    return decrypted

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())