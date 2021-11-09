camel = input()
snake = []
underscore = "_"

for character in camel:
    if character.isupper():
        snake.extend((underscore, character.lower()))
    else:
        snake.append(character)

print("".join(snake))
