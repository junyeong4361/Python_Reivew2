# type_method.py

'''
    자료형별 함수 제공

        1. 숫자형 함수
            int() : 정수로 변환
            float() : 실수로 변환

        str() : 문자열로 변환
        list() : 리스트로 변환
        tuple() : 튜플로 변환
        dict() : 딕셔너리로 변환
        set() : 집합으로
        bool() : True/False
        
'''

# int() (많이 씀)
str1 = "123"

print(int(str1)+ 10)

num = 10.123
print(int(num))

num = int(str1)
print(num+10)

str1 = "123a"
# int(str1) 문자 안에 숫자만 있어야함

num = "10.123"
# print(int(num)) 문자열 실수는 int()로 변경이 불가능

# float() (많이 씀)
print(float(num))
num = "30"

print(float(num))
print()

# str()
print(str(100)+ "만원")
print()

#list()
str1 = "abcd"
print(list(str1))

# tuple()
print(tuple(str1))

# dict(k=v, k=v, ...)
print(dict(a=10, b=20))

# set()
str1 = "aabbcc"
print(set(str1))






















