cafe_out = ""
max_cats = 0

while True:
    cafe_stats = input().split()
    if cafe_stats[0] == "MEOW":
        print(cafe_out)
        break
    cats_in = int(cafe_stats[1])
    if cats_in > max_cats:
        max_cats = cats_in
        cafe_out = cafe_stats[0]
