# input.py

'''
    [입력 받는 함수 input]
        > 프로그램에서 값을 입력 받고, 유동적인 코드를 작성
        (입력된 값에 따라서 결과가 달라진다)

    [input()함수의 실행 과정]
        1. input() 사용 -> '입력 대기 상태'
        2. 입력 후 엔터
        3. input() 함수에 의해, 입력된 내용이 '문자열'로 반환
'''
# 1. 그냥 쓰기

'''
input() # 입력한 값으로 바뀐다. (문자열)
"abc"
'''


# 2. 변수에 대입
'''
str1 = input() # input() -> 문자열
print("입력한 값 : " + str1)
'''

# 3. print()함수에 안에서 바로 출력
'''
print("입력한 값2 :" + input())
'''

# 4. input() 함수의 출력 기능
'''
print("이름을 입력하세요 :", end="")
name = input()
print(f"입력하신 이름은 {name}입니다.")
'''

# input("입력 받기 전 출력할 문구")
'''
name = input("이름을 입력하세요 : ")
print(f"입력하신 이름은 {name}입니다.")
'''

# input()은 문자열이라서 문자열의 함수를 사용
'''
print("a의 개수 :", input("문자를 입력 :").count("a"))
'''

# 5. 입력된 값을 숫자로 다루겠다.
'''
str1 = "123"
num = int(str1)

num1 = input("숫자 입력: ")
num1 = int(num1)
print("num1 + 10 =", num1+10)
'''

# 6. 입력과 변환을 한 번에
'''
num = int(input("숫자 입력 : "))
print(num * 10)
print()
'''

# 7. 여러 값을 한 번에 입력 받고 정수로 변환하고 싶다.
'''
    split(), map() 함수 필요

    split() : 기준 되는 문자로 대상 문자열을 나눠서 리스트로 반환
        > 기준이 없다면 공백, 개행으로 나눈다.

    map() : 함수를 여러 번 반복 시킨다.
    map(반복 수행할 함수의 이름, 요소가 여러 개인 값)
    
'''

a, b = map(int, ["1", "2"])
# a,b = int("1"), int("2")
# a,b = 1, 2
print(a+b)
print()

num1, num2 = map(int, input("두 수 입력 : ").split())
# 1. "두 수 입력 : " 출력
# 2. 입력 대기 상태 -> 입력 후 엔터 (3 5)
# 3. 입력한 값이 '문자열'로 돌아온다.
#   num1, num = map(int, "3 5".split())

# 4. 문자열.split()의해 "3 5" 문자열이 리스트 자료형으로 바뀐다.
#    num1, num2 = map(int, ["3", "5"])

# 5. map()함수가 동작하면서 int가 각각의 요소에 적용
#   num1, num2 = int("3"), int("5")
#   num1, num2 = 3, 5
print(num1 + num2)
print()

# 1. 문자열 입력
str1 = input("문자열 입력 : ")

# 2. 숫자 하나씩 입력
num1 = int(input("숫자 입력 : "))

# 3. 여러 숫자를 한번에 입력
num1, num2, num3  = map(int, input("여러 수 입력 : ").split())

# 입력 연습

'''
    1. 사각형 면적 구하기
        가로,세로를 입력 받고 면적을 출력

    [출력결과]
    가로, 세로 입력 : 4 5
    면적은 20입니다.
'''

# print( "면적은 {}입니다.".format(??) )

num1, num2 = map(int, input( "가로, 세로 입력 :").split())
num3 = num1 * num2
print("면적은 {}입니다.".format(num3))















