import itertools

for a,b,c,d in itertools.permutations("abcd", 4):
    print(a+b+c+d)