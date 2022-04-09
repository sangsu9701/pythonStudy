# Chapter03-4
# Python Tuple
# 리스트와 비교
# 튜플 자료형(순서O, 중복O, 수정X, 삭제X) # 불변 (java - 상수값 같은)

# 선언

a = ()
b = (1,) # 한개일때는 마지막이 콤마로 끝나여야함
c = (11, 12, 13, 14, 15)
d = (100, 1000, 'Ace', 'Base', 'Captain')
e = (100, 1000, ('Ace', 'Base', 'Captain'))

# Indexing
print('>>>>>>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('e - ', e[-1])
print('e - ', e[-1][1])
print('d - ', list(e[-1][1]))

# 수정X
# d[0] = 1500

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:1])
print('d - ', e[2][1:3])

# 튜플 연산
print('>>>>>>')
print('c + d ', c + d)
print('c * 3 ', c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4, 2)
print('a - ', a)
print('a - ', a.index(3))
print('a - ', a.count(2))

# 패킹 & 언패킹 ( Packing and Unpacking )
# Packing : 패키징 하는 것

# 패킹
t = ('foo', 'bar', 'baz', 'qux')

print(t)
print(t[0])
print(t[-1])

# 언패킹1
(x1, x2, x3, x4) = t # 각각에 할당해주는 방법
xx1, xx2, xx3, xx4 = t # 와 같이 () 가 없어도 언패킹이 되지만 관습상 () 처리를 해줌
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 패킹 & 언패킹
t2 = 1, 2, 3 # 와 같이 () 를 안해줘도 튜플이다
t3 = 4, # -> 패킹
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)