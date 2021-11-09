pancakes = 1
while pancakes > 0:
    print("I'm the happiest human being in the world!")
    pancakes -= 1
    if pancakes == 0:
        print("Now I have no pancakes!")
#        break
else:
    print("No pancakes...")

pets = ['dog', 'cat', 'parrot']
for pet in pets:
    print(pet)
else:
    print('We need a turtle!')

counter = 0
max_value = 0
while counter < 10:
    counter = counter + 1
    max_value = max_value + counter
    if max_value > 15:
        break
    counter = counter + 1

print(counter)