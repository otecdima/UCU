shift = 3 # defining the shift count

text = "computer"

encryption = ""

for c in text:

    # check if character is an uppercase letter
    if c.isupper():

        new_index = (ord(c) - ord("A") + shift) % 26
        new_unicode = new_index + ord("A")
        new_character = chr(new_unicode)
        encryption = encryption + new_character

    else:

        # since character is not uppercase, leave it as it is
        c_unicode = ord(c)

        c_index = ord(c) - ord("a")

        # perform the shift
        new_index = (c_index + shift) % 26

        # convert to new character
        new_unicode = new_index + ord("a")

        new_character = chr(new_unicode)

        # append to encrypted string
        encryption = encryption + new_character
        
print("Plain text:",text)

print("Encrypted text:",encryption)
