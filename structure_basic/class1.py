# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전

시퀀스 - in 연산자 사용 가능
"""

# 멀티라인 입력
multi_str = \
'''
String
multi
line
'''
print(multi_str)

# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('n' in str_o2)
print('P' not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수(upper, inalnum, startswith, count, endswith, isalpha ...)

# 첫 문자를 대문자로
print("Capitalize : ", str_o1.capitalize());
# ~으로 끝났는지
print("endswith?: ", str_o2.endswith("e"))
# 문자 대체
print("replace : ", str_o1.replace("thon", "Good"))
# 리스트 형태로 변환
print("sorted: ", sorted(str_o1))
print("split: ", str_o4.split(' '))

# 반복(시퀀스)
im_str = "Good Boy!"
# im_str에서 사용할 수 있는 것들을 나열 (__iter__ 가 있다면 반복이 가능하다는 뜻), 속성을 보여주는 명령어
print(dir(im_str)) # __iter__ 

# 출력
for i in im_str:
    print(i)


# 슬라이싱
str_s1 = "Nice Python"

print(len(str_s1)) # 11

# 슬라이시 연습
print(str_s1[0:3]) # index -> [x:y-1] -> 0~2 인덱스까지 나온다
print(str_s1[5:11]) 
print(str_s1[5:])
print(str_s1[:len(str_s1)])
print(str_s1[1:4:2]) # 1부터 4까지 2칸씩 가져와라
print(str_s1[-5:]) #맨 오른쪽부터 -1 씩
print(str_s1[1:-2])
print(str_s1[::2])
print(str_s1[::-1])

# 아스키 코드(또는 유니코드)
a = 'z'

print(ord(a)) # 아스키 코드로
print(chr(122)) # 문자로