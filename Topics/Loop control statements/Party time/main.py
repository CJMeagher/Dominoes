guest_names = []

while True:
    guest_name = input()
    if guest_name == ".":
        break
    guest_names.append(guest_name)

print(guest_names)
print(len(guest_names))
