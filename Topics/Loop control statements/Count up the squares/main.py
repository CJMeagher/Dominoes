sum_of_input = 0
sum_of_squares = 0

while True:
    integer_in = int(input())
    sum_of_input += integer_in
    sum_of_squares += integer_in ** 2
    if sum_of_input == 0:
        break

print(sum_of_squares)
