#06‑2 3 과 5 의 배수를 모두 더하기
#10 미 만 의 자 연 수 에 서 3과 5의 배 수 를 구 하 면 3, 5, 6, 9이 다. 이 들 의 총 합 은 23이 다.
#1,000 미 만 의 자 연 수 에 서 3의 배 수 와 5의 배 수 의 총 합 을 구 하 라.

#3의배수 + 5의배수 - 3,5의 공배수 빼기

#배수 갯수를 구하는 함수
def multiple(whole,n):
    count = 0
    multiplesum = 0
    while count < (whole-1)//n:
        count+=1
        multiplesum += count*n
    return multiplesum

#입력받기 : 1000미만의 자연수
nnumber = int(input("1000미만의 자연수를 입력하세요 : "))

if nnumber >= 1000:
    print("1000미만의 자연수를 입력하세요")
else :
    result = multiple(nnumber,3) + multiple(nnumber,5) - multiple(nnumber,15)
    print(result)

