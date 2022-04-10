# Chapter 04-3
# 파이썬 반복문
# While 실습

# While <expr>:
#   <statement(s)>

# 예제 1
n = 5
while n > 0:
    print(n)
    n = n - 1

# 예제 2
a = ['foo', 'bar', 'baz']

while a:
    print(a.pop(-1)) # pop() == pop(-1) 둘 다 같은 의미이지만 명시적으로 -1을 적어준다.


# 예제 3
# break, continue

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Ended.')
print()

# 예제 4

m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(n)
print('Loop Ended.')
print()


# 예제 5
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break;
else:
    print('else out.')