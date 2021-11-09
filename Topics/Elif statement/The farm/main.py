CHICKEN, GOAT, PIG = 23, 678, 1296
COW, SHEEP = 3848, 6769

money = int(input())
animals = 0
animal = "None"

if money >= SHEEP:
    animals = money // SHEEP
    animal = "sheep"
elif money >= COW:
    animals = money // COW
    animal = "cow"
elif money >= PIG:
    animals = money // PIG
    animal = "pig"
elif money >= GOAT:
    animals = money // GOAT
    animal = "goat"
elif money >= CHICKEN:
    animals = money // CHICKEN
    animal = "chicken"

if animals > 0:
    print(animals, animal + ("s" if animals > 1 and animal != "sheep" else ""))
else:
    print(animal)
