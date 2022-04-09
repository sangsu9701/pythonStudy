# Chater03-3
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(쑨서 O, 중복 O, 수정 O, 삭제 O()

# 선언
a = []
b = list()
c = [70, 75, 80, 85] # len
d = [1000, 10000, 'Ace', 'Base', 'Captain']
e = [1000, 10000, ['Ace', 'Base', 'Captain']]
f = [21.42, 'foobar', 3, 4, False, 3.141592]

# Indexing
print('>>>>>>')
print('d - ', type(d), d)
print('d - ', d[0] + d[1], d[2])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()

# Identity(id)
temp = c # 리스트의 주소값을 공유한다
print(temp, c)
print(id(temp))

print(id(c))

# 리스트 수정, 삭제
print('>>>>>')
c[0] = 4
print(' c - ', c)
c[1:2]  = ['a', 'b', 'c'] # [['a', 'b', 'c']]
print('c - ', c) # list 안에 원소들이 들어감. (중첩이 발생X)
c[1] = ['a', 'b', 'c'] # list 안에 list가 들어감. (중첩이 발생) - [[]] 처럼 두개 쓴 것과 같은 효과
print('c - ', c)
c[1:3] = [] # 삭제
print('c - ', c)
del c[2] # 삭제
print('c - ', c)

# list 함수
a = [5, 2, 3, 1, 4]
print('a - ', a)
a.append(6)
print('a - ', a)
a.sort() # 내부 알고리즘에 의해 되는 것이므로 데이터가 굉장히 커지면(1억개 이상) 오래 걸린다
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(3), a[3]) # index로 가져올 수 있는 2가지 방법
a.insert(2, 7)
del a[6] # 매우 비효율적인 delete 방법
print('a - ', a)
a.remove(5) # 해당 값을 가진 인덱스 삭제
print('a - ', a)
a.append(3)
print('a - ', a)
a.remove(3) # 인덱스가 빠른것부터 삭제
print('a - ', a)

print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(6))


# append: 맨 마지막에 추가, insert: 해당 인덱스에 값을 넣고 나머지 뒤로 밀기
# 삭졔: remove, pop, del

while a:
    data = a.pop()
    print(data)
