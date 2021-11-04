def total_occurrences(s1, s2, ch):
    for ch in s1 and s2:
        if ch in s1 and ch in s2:
            number = s1.count(ch)
            number1 = s2.count(ch)
            finalnumber = number + number1
            return (print(finalnumber))
        elif ch not in s1 or ch not in s2:
            return None

total_occurrences('color', 'yellow', 'l')
# total_occurrences('red', 'blue', 'l')
# total_occurrences('green', 'purple', 'b')