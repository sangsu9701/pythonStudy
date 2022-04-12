# Chapter 06-1
# 파이썬 클래스
# OOP(객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해
# 하나의 틀(클래스)를 가지고 코드상에서 변수로 할당해서 메모리에 올라가고 
# ID값을 갖는 그 시점 / 어떤 변수로 활용할 수 있는 대상 / 설계도를 바탕으로 구현된 것을 인스턴스 화 되었다고 한다
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간 (딕셔너리 형태로 저장)
# 클래스 변수: 직접 접근 가능, 공유한다
# 인스턴스 변수 : 객체마다 별도 존재

# 예제 1
class Dog: # Object 상속 3가지 방법 존재 (class Dog():, class Dog(Object):, class Dog: pass)
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age): # 클래스가 초기화되면 반드시 한번 호출되는 함수
        self.name = name
        self.age = age


# 클래스 정보
print(Dog)

# 인스턴스화
a = Dog("micky", 2)
b = Dog("baby", 3)

# 비교
print(a == b, id(a), id(b))

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)
print('dog', Dog.species)
print('dog1', a.species)


# 예제2
# self의 이해
class SelfTest:
    def func1(): # 암묵적으로 클래스 내부에 매개변수를 선언하는데 셀프가 없다 이런 것은 클래스 메소드이다.
        print('Func1 called')
    def func2(self): # self는 인스턴스를 요구. self 에 f가 넘어간 것
        print(id(self))
        print('Func2 called')


f = SelfTest()

# f 안에 있는 모든것을 보기 위함
# 사용자가 사용할 수 있는 메서드가 들어있는데 func1, func2가 추가되어있는 모습을 확인할 수 있다

#print(dir(f))
#print(id(f))

#f.func1() 예외
f.func2()  # 인스턴스화 시켜서 호출하면 바로 알아서 self 로 id 가 f의 인스턴스 값으로 넘어간다

SelfTest.func1() # 클래스로 바로 접근해서 호출할 수 있는 메소드
#SelfTest.func2() 예외 발생
SelfTest.func2(f) # 클래스로 바로 접근해서 호출할 때 self 가 없다 하면 생성한 인스턴스를 넣어주면 된다


#### 클래스 메소드는 self 가 없는것. 클래스로 직접 호출 - 아무 매개변수가 없기 때문에
#### self가 붙은 것은 인스턴스 메소드. 인스턴스를 넘겨주던가 인스턴스로 호출해야 한다.

# 예제 3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # class variable
    stock_num = 0 # 재고

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num) # 결과 : 2 // 인스턴스가 2개 생성되었기 때문에

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)
print('>>>>', user1.stock_num) # user1에는 없지만 없을땐 warehouse class의 namespace에 가서 알아서 찾는다.

del user1
print('after', Warehouse.__dict__)

# 예제 4
class Dog2: 
    species = 'firstdog'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)
    
    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)


# 인스턴스 생성
c = Dog2('july', 4)
# 메소드 호출
print(c.info())
# 메소드 호출
print(c.speak('Wal Wal'))