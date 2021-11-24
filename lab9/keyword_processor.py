"""Lab 9.1"""
def find_film_keywords(film_keywords: dict, film_name: str):
    '''
    Finds keywords in a particular film
    >>> find_film_keywords({'Marvel': ['Spiderman', 'Avengers: Endgame', \
'Wandavision'], 'Sony': ['Spiderman', 'Wandavision', 'What If']}, "Spiderman") #doctest: +ELLIPSIS
    {...
    '''
    final_list = []
    for key_indict in film_keywords:
        values_of_dict = film_keywords[key_indict]
        if film_name in values_of_dict:
            final_list.append(key_indict)
    sett = set(final_list)
    return sett
# print(find_film_keywords({'Marvel': ['Spiderman', 'Avengers: Endgame'], 'Sony': ['Spiderman', 'Wandavision', 'What If']}, "Spiderman"))

def find_films_with_keywords(film_keywords: dict, num_of_films: int):
    '''
    Returns films with most coincides
    >>> find_films_with_keywords({'Marvel': ['Spiderman', 'Avengers: Endgame' \
'Wandavision'], 'Sony': ['Spiderman', 'Wandavision', 'What If']}, 2)
    [('Spiderman', 2), ('What If', 1)]
    '''
    newdict = {}
    newlist = []
    if num_of_films == 0:
        return []
    for _, values in film_keywords.items():
        for value in values:
            if value not in newdict:
                newdict[value] = 1
            else:
                newdict[value] = newdict[value] + 1
    newlist = list(newdict.items())
    newlist.sort(key=lambda x: x[1])
    newlist.reverse()
    newlist = newlist[:num_of_films]
    return newlist
# print(find_films_with_keywords({'Marvel': ['Spiderman', 'Avengers: Endgame'], 'Sony': ['Spiderman', 'Wandavision', 'What If']}, 2))


import doctest
print(doctest.testmod())