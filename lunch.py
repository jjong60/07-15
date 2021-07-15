import random #random이라는 이름의 꾸러미를 사용할것임을 뜻함.
# ctrl + / : 선택문장 주석처리 단축키
# 리스트 활용하기
# menu 변수에 '한식', '일식', '중식', '양식' 의 값을 순차적으로 저장하기
# list는 가변, array는 고정길이를 가진다.
menu = ['한식', '일식', '중식', '양식']
# menu.append(8)
# print(menu[0])

# 파이썬에서는 기본 제공되는 기능들이 많음
# 임의의 값을 뽑아오는 기능도 있음 : random
# 기능들을 사용하려면 불러와서 사용해야함 : import
lunch = random.choice(menu)
# print(lunch)

number = {'중식' : '123-456', '한식' : '789-123', '양식' : '123-456', '일식' : '789-123'}
# print(number[lunch])

# 오늘의 점심은 @@@@입니다. 전화번호는 @@@@-@@@@ 입니다.
print('오늘의 점심은 ',lunch,'입니다. 전화번호는 ', number[lunch], '입니다.')
print(f'오늘의 점심은 {lunch}입니다. 전화번호는 {number[lunch]}입니다.')