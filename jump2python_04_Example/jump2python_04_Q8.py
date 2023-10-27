import sys

numbers = sys.argv[1:]

sum = 0
if numbers:
    for i in numbers:
        sum += int(i)

print(sum)