# Chapter04-1
# 파이썬 제어문
# IF 실습

# 기본 형식
print(type(True)) # 0이 아닌 수, "abc", [1, 2, 3..], (1, 2, 3..) ..
print(type(False)) # 0, "", [], (), {} ..

# 에1

if True:
    print('Good') # 무조건 들여쓰기 할 것. 아니면 에러

# 에2
if False:
    print("Bad!")
else:
    print("Good!")

# 예3
city = ""
if city:
    print("You are in : ", city)
else:
    print("plz enter ur city")

# 예4
id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin':
    print('관리자 입장')

# 예5
# 다중조건문

num = 90

if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else: 
    print('F')


# in, not in

q = [10, 20, 30]
w = {70, 80, 90, 100}
e = {"name": "Lee", "city": "Seoul", "grade": "A"}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e) # key 중에 탐색
print("Seoul" in e.values())
