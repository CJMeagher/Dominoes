fizz = "Fizz"
buzz = "Buzz"
start_range = 1
end_range = 101

for i in range(start_range, end_range):
    out = ""
    if (i % 3) == 0:
        out = fizz
    if (i % 5) == 0:
        out += buzz
    print(i if out == "" else out)
