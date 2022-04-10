# Chapter04-2
# 파이썬 반복문
# For 실습

# for in <collection>
#   <Loop body>


for v1 in range(10): # N-1 (0~9 까지)
    print('v1 is : ', v1)

print()

for v2 in range(1, 11):
    print('v2 is : ', v2)

print()

for v3 in range(1, 11, 2):
    print('v3 is : ', v3)

# 1~ 1000합
sum1 = 0
for v in range(1, 1000):
    sum1 += v

print('1 ~ 1000 sum : ', sum1)
print('1 ~ 1000 sum : ', sum(range(1, 1001)))

print(range(1,11))
print(type(range(1,11))) # Generator, Iterator


# Iterables : 반복할 수 있는 객체  
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for n in names:
    print('You ar : ', n)

# 예제2 - 리스트
lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print("Current number : ", n)

# 예제3 - 문자열
word = "Beautiful"

for s in word: 
    print('word : ', s)

# 예제4 - 튜플
my_info = {
    "name": 'Lee',
    "Age": 33,
    "City": "Seoul"
}

for key in my_info:
    print('key : ', my_info)
    print('value : ', my_info[key])
for v in my_info.values():
    print('value : ', v)

# 예제5
name = "FineaApplE"

for n in name:
    if n.isupper():
        print(n)
    else: 
        print(n.upper())

# for - else # 파이썬에만 독보적으로 있는 구문

numbers = [14, 3, 4, 5, 8, 24, 12, 124, 21, 36, 84, 45]

for num in numbers:
    if num == 24:
        print("Found : 24")
        break
else: # for문을 끝까지 돌고 나서 딱 한번 실행
    print('Not Found : 24')


# 구구단
for i in range(1,10):
    for j in range(1, 10):
        print(i, " * ", j, " = ", i*j)

for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}' .format(i*j), end='')
    print()


# 변환 예제
name2 = 'Aceman'

print('Reversed', reversed(name2))
print('List', list(reversed(name2)))