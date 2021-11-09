units = int(input())
no, few, pack, horde, swarm = 1, 9, 49, 499, 999

if units < no:
    print("no army")
elif units <= few:
    print("few")
elif units <= pack:
    print("pack")
elif units <= horde:
    print("horde")
elif units <= swarm:
    print("swarm")
else:
    print("legion")
