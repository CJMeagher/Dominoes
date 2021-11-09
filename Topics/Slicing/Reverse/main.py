# the following line reads the list from the input; do not modify it, please
numbers = [int(num) for num in input().split()]
start = 16
stop = 3
step = -1
print(numbers[start:stop:step])  # the line with an error
