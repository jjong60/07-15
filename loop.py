dust = [49,55,80,75,39]

# print(dust[0])
# print(dust[1])
# print(dust[2])
# print(dust[3])
# print(dust[4])

i = 0
while (i < 5):
    print(dust[i])
    i += 1


#for : 특정 횟수가 정해져 있을 경우 사용 >> 리스트의 길이만큼 반복 포함
for e in dust:
    print(e)
    #e가 리스트의 요소 하나를 가리킴

# while문과 같이 반복 계수를 이용해서 인덱스에 접근하여 출력
for i in range(5): # i는 0~4까지 증가하는 수
    print('for문입니다.')
    print(i)
    print(dust[i])
    