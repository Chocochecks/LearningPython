#Q2 3 의 배수의 합 구하기
#while 문을 사용해 1 부터 1000 까지의 자연수 중 3 의 배수의 합을 구해 보자.

result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result) # 166833 출 력



