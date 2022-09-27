def translate(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEIOU":
            translation=translation+"V"
        else:
            translation=translation + letter
    return translation

print(translate(input("Enter A Phrase: ")))
