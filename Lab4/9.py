username = input("")
disallowed_characters = username

for character in disallowed_characters:
    username = username.replace(character, "*")

print(username)