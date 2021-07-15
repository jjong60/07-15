import random

numbers = range(1,46) # 0,1,2,3,4 
#range(a,b) : a는 범위에 포함되고 뒤쪽은 포함되지 않음 a는 0일때 생략가능
# print(numbers)
#random.sample(seq, k) : 시퀀스에서 랜덤한 중복되지 않는 길이 k의 리스트를 반환
lotto = random.sample(numbers,7)

print('로또 번호는 ', lotto)
# 3개 맞으면 5등
# 4개 맞으면 4등
# 5개 맞으면 3등