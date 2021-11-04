def merge_teh_tools(string, k):
    for i in range(0, len(string), k):
        st = string[i:i+k]
        rez = ''
        for char in st:
            if char not in rez:
                rez = rez + char
        print(rez)