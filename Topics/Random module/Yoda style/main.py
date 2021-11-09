import random


sentence = input().split()
seed_value = 43
random.seed(seed_value)
random.shuffle(sentence)
print(' '.join(sentence))
