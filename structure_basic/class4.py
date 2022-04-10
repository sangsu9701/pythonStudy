# Chapter03-5
# Python Dictionary
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서X, 키 중복X, 수정O, 삭제O)

# 선언
# a = {'name': 'Kim', 'name' : 'Lee'} # key 값은 중복이 되면 안된다.
a = {'name': 'Park', 'phone':'01012341234', 'birth':'970109'}
b = {0: 'Hello World'}
c = {'arr': [1, 2, 3, 4]}
d = { # Java에서 Json형태와 비슷
    'Name': 'NiceMan',
    'City': 'Seoul',
    'Age': 26,
    'Grade': 'A',
    'Status': True
}

e = dict([ # 잘 사용하지는 않지만 FM대로 표현하는 방법 (list 안에 tuple 이 들어 있다)
    ('Name', 'NiceMan'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade', 'A'),
    ('Status', True)
])

f = dict( # 주로 d f 방법 많이 사용, Java 에서는 Map
    Name='NiceMan',
    City='Seoul',
    Age=27,
    Grade='A',
    Status=True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)


# 출력
print('a - ', a['name']) # key가 없다면 type error 발생. 프로그램이 끊김
print('a - ', a.get('name1')) # get으로 가져오면, key가 없어도 None으로 출력해줌. 프로그램이 끊기지는 않음
print('b - ', b[0])
print('b - ', b.get(0))
print("f - ", f.get('City'))
print("f - ", f.get('Age'))

# 딕셔너리 추가
a['address'] = 'seoul' # 동일한 key가 존재한다면 기존 값을 지우고 이 값을 넣어줌
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

# 딕셔너리 개수
print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))

# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용 가능
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())
print('a - ', list((a.keys())))
print('b - ', list((b.keys())))

print()

print('a - ', a.values())
print('b - ', b.values())

print()

print('a - ', a.items())
print('b - ', b.items())

print()

print('a - ', a.pop('name'))
print('a - ', a)

print()

print('f - ', f.popitem()) # 임의의 하나의 아이템을 없앤다
print('f - ', f)
print('f - ', f.popitem()) # 계속 반복되어서 빈 값이 되더라도 에러가 발생하더라도 프로그램은 끊기지 않는다 


print('a - ', 'birth' in a)
print('d  - ', 'City' in d)

# 수정
a['address'] = 'test_dict'
print('a - ', a)

a['address'] = 'dj'
print('a - ', a)

a.update(birth='231231')
print('a - ', a)
temp = {'address': 'Busan'}

a.update(temp)
print('a - ', a)