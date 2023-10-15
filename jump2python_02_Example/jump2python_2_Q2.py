## 점프 투 파이썬 2장 되새김 문제

#Q2 홀수, 짝수 판별하기
numberInput = input("숫자를 입력하세요 : ")
isOdd = int(numberInput)%2
if isOdd:
    print("홀수입니다.")
else:
    print("짝수입니다.")