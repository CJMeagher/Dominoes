floats = []

while True:
    string_in = input()
    if string_in == ".":
        if floats:
            print(min(floats))
        break
    else:
        floats.append(float(string_in))
