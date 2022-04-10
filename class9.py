# Chapter 05-1
# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def function_name(parameter):
#   code

# 예제1
def first_func(w):
    print("Hello, ", w)

word = "Goodboy"

first_func(word)


# 예제2
def return_func(w1):
    return "Hello, " + str(w1)

x = return_func('Goodboy2')
print(x)

# 예제3 (다중 반환)
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = func_mul(10)


# 튜플 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

q = func_mul2(20)

print(type(q), q, list(q))


# 딕셔너리 리턴
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1' : y1, 'v2' : y2, 'v3' : y3}

d = func_mul3(30)

print(type(d), d, d.get('v2'), d.items(), d.keys())


# 중요
# *args, **kwargs

# *args(언팩킹) -> 전송하는 매개변수를 동적으로 튜플형태로 받아 언팩해서 사용 (가변 인자)
# 튜플
def args_func(*args): # 매개변수 명은 자유
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('-----')

args_func('Lee')
args_func('Lee', 'Park')

# **kwargs(언패킹)
# 딕셔너리 형태 (key, value)
def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('------')

kwargs_func(name1='Lee', name2='Park')

# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park', age1=20, age2=30, age3 = 40)


def nested_func(num):
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num + 100)

nested_func(100)