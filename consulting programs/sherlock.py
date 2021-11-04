st1 = 'aabbcd'
st2 = 'aabbccddeefghi'
st3 = 'abcdefghhgfedecba'

def isValid(st):
    counter = [0]*26

    for char in st:
        if counter[ord(char) - ord('a')] < 1:
            counter[ord(char) - ord('a')] = st.count(char)
    
    count = 0
    for i in counter:
        if (i and i != counter[0]) and count == 1:
            return "No"
        elif i and i != counter[0]:
            count = count + 1
    
    if count == 0 or count == 1 or count == len(st) - 1:
        return "Yes"

isValid(st1)
isValid(st2)
isValid(st3)