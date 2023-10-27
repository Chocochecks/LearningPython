def avg_number(*numbers):
    result = 0
    for i in numbers:
        result += i
    return result/len(numbers)

print(avg_number(1,2,3,4,5))
print(avg_number(1,2))