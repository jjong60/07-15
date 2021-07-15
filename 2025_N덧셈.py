# input() >> 한 줄 입력받기
# input()의 결과는 문자열로 입력받음 >> 정수형 문자열로 바꿔야함
N = int(input())

i = 1
#계속 누적 합을 알고있어야함
#누적합을 저장할 변수를 하나 선언해야함
result = 0 # 아무것도 더하지 않으면 0이니까 0으로 초기화
while i <= N:
    result = result + i
    i = i + 1
    
print(result)