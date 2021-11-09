integers = []

while True:
    string_in = input()
    if string_in == ".":
        print(sum(integers) / len(integers))
        break
    else:
        integers.append(int(string_in))
