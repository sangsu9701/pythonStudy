# Chapter03-6
# 집합(Set) 특징
# 집합(Set) 자료형(순서X, 중복X)

# 선언
a = set()

print(type(a))

b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'} # tuple에 key가 없다면 집합(set)
f = {42, 'foo', (1, 2, 3), 3.141592}

print('a - ', type(a), a, 2 in a)
print('a - ', type(b), b)
print('a - ', type(c), c)
print('a - ', type(d), d)
print('a - ', type(e), e)
print('a - ', type(f), f)

# 튜플 변환(set -> tuple)
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])


# 리스트 변환(set -> list)
l = list(c)
l2 = list(e)

print('l - ', l)
print('l - ', l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

print()

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8 ,9])
s3 = set([3, 4])

print('s1 & s2 : ', s1 & s2)
print('s1 & s2 : ', s1.intersection(s2))

print('s1 | s2 : ', s1 | s2)
print('s1 | s2 : ', s1.union(s2))

print('s1 - s2 : ', s1 - s2)
print('s1 - s2 : ', s1.difference(s2))

# 중복 원소 확인
print('s1 & s2 : ', s1.isdisjoint(s2)) # 교집합이 없는가? yes - true, no - false

# 부분 집합 확인
print(s1.issubset(s3))
print(s3.issubset(s1))
print(s1.issuperset(s3))

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 - ', s1)

s1.remove(2)
print('s1 - ', s1)
# s1.remove(7) ## 오류 발생 O 

s1.discard(3)
print('s1 - ', s1)
# s1.discard(7) ## 오류 발생 X - 예외를 발생시키지 않는다 

s1.clear()