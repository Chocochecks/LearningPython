import random
x=0
list = []
while (x < 6):
    value = random.randint(1,45)
    if value not in list:
        list.append(value)
        x+=1

print(list)