# 모듈 사용 실습

import sys
import time

print(sys)
print(sys.path)
print(type(sys.path))

sys.path.append('D:\selfStudy\pythonStudy\module')

print(sys.path)

import test_module

print(test_module.power(10, 3))


print(time.time())

