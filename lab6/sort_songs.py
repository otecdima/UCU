"""Sorting songs"""
from typing import List, Tuple, Callable, Union

def sort_songs(
    song_titles: List[str],
    length_songs: List[str],
    key: Callable[[tuple], Union[int, str, float]]) -> List[tuple]:
    """
    Sorts songs
    >>> sort_songs(['Я на небі був', 'Той день', 'Африка', 'Коли тебе нема'], \
    ['3.19', '3.58', '5.06', '4.31'], last_word)
    [('Африка', '5.06'), ('Я на небі був', '3.19'), ('Той день', '3.58'), \
('Коли тебе нема', '4.31')]
    """
    if len(song_titles) == len(length_songs):
        new_tuple = [(song_titles[i], length_songs[i]) for i in range(len(song_titles))]
        return sorted(new_tuple, key = key)
    else:
        return None
    

def song_length(new_tuple: Tuple[str]) -> float:
    """
    Sorts for song's length
    """
    new_tuple1 = new_tuple[1]
    return new_tuple1

def title_length(new_tuple: Tuple[str]) -> int:
    """
    Sorts for title length
    >>> print("Hello world!")
    Hello world!
    """
    new_tuple2 = len(new_tuple[0])
    return new_tuple2

def last_word(new_tuple: Tuple[str]) -> str:
    """
    Sort for the first letter of the last word
    >>> print("Hello world!")
    Hello world!
    """
    new_tuple3 = new_tuple[0].split(" ")[-1]
    return new_tuple3


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

