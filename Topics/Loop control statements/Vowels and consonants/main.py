for char in input():
    if char.isalpha():
        print("vowel" if char.lower() in "aeiou" else "consonant")
    else:
        break
