import random
import itertools

person = ['김 승 현', '김 진 호', '강 춘 자', '이 예 준', '김 현 주']
chores = ['청 소', '빨 래', '설 거 지']

random.shuffle(person)

print(list(itertools.zip_longest(person, chores, fillvalue="휴식")))