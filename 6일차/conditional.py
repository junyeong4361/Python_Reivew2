# conditional.py


'''
     제어문 - 조건문, 반복문
         > 코드를 상황에 따라 제어한다. (프로그램의 흐름을 제어한다.)

    [조건문]
        > 조건을 판단하여 상황에 맞게 처리

        if문 : 만약, ~~면
            '만약' 조건에 만족하면 수행해라!
                만족한다 = True
                만족하지x = False


    [비교 연산자]
        조건식에 자주 사용되는 연산자
        조건에 만족하면 결과 값이 True, 아니면 False

        a > b  a가 b보다 크냐?
        a < b  a가 b보다 작냐?
        a >= b a가 b보다 크거나 같냐?
        a <= b a가 b보다 작거나 같냐?
        a == b a와 b가 같냐?
        a != b a와 b가 다르냐?
        
'''
# 비교연산자
print(3 > 0)
print(3 < 0)
print(3 >= 0)
print(3 <= 0)
print(3 == 0)
print(3 != 0)

print("abc" == "abc")
print("abc" != "abc")
print()


'''
    [논리 연산자]
        a or b      a 또는 b 중에 하나라도 참이면 참 / 둘 다 거짓이면 거짓
        a and b     a와 b 둘 다 참이어야 참 / 둘 중 하나라도 거짓이면 거짓
        not a       a가 참이면 거짓으로 / 거짓이면 참으로 (참과 거짓을 뒤집는다)
'''

# 논리 연산자
print(3 > 0 or 2 < 0)
print(3 < 0 or 2 < 0)

print(3 > 0 and 2 < 0)
print(3 > 0 and 2 > 0)

num = 31

print(num > 10 and num < 30) # 10보다 크고 30보다 작은 수

print(not num > 30)
print()

'''
    [포함 연산자]
        a in b      b 안에 a가 있으면 참 / 없으면 거짓
        a not in b  b 안에 a가 없으면 참 / 있으면 거짓

        b에는 요소가 여러 개인 자료형의 값이 위치한다. (리스트, 튜플, 문자형 등등)
'''

# 포함 연산자

print("A" in "ABCD")
print("AB" in "ABCD")
print("A" in ["AB", "ABC", "ABCD"])

print("A" not in ["AB", "ABC", "ABCD"])


'''
    [if문 기본 구조]
    if 조건식:
        수행문
    elif조건식2:
        수행문2

    elif조건식3:
        수행문3

    else:
        수행문4

        1. 조건식
            참이나 거짓이 있어야 한다. (식의 결과가 T/F)
            조건식의 끝에는 콜론(:)을 붙인다.
            콜론의 뒤부터는 수행문으로 간주한다.

        2. 수행문
            조건식이 만족할 때 수행하는 코드를
            반드시 '들여쓰기'를 해야한다. -> 기본 공백 4개 발생
            수행문 코드 간의 들여쓰기가 맞지 않으면 오류 발생

            들여쓰기만 맞으면 수행문을 여러 줄 작성할 수 있고
            들여쓰기를 끝내면 if문의 수행문이 끝난 것

        3. elif 조건식 :         (else if) 다른 만약
            위 조건식이 만족하지 않으면 이 조건식은 만족하는가?
            if문에 종속된다. (if문 없이 바로 사용 할 수 없다.)
            여러 개 사용 가능

        4. else:
            위 조건식이 만족하지 않으면 '무조건' 여기를 수행해라!
                >조건식이 없다.
            if문에 종속
            하나만 사용할 수 있다.
'''
"""
num = 3
if num > 0:
    print("3은 0보다 크다.")
#print("끝!")
#print("수행문!")

if 4 in [1, 2, 3, 4]: print("4")


print()

# 숫자를 입력 받아 음/0/양
"""
'''
num = int(input("숫자 입력 : "))

if num > 0:
    print("양수")
elif num < 0:
    print("음수")
#elif num == 0:
#    print("0이다.")
else: # 조건식이 없어서 연산 없이 무조건 진입
    print("0이다.")

'''
# 점수를 입력 받아 학점을 출력
'''
    100점 -> A+
    90~99 -> A
    80~89 -> B
    70~79 -> c
    60~69 -> D
    60미만 -> F
    0 -> (빵점)F
'''
'''
score = int(input("점수 입력: "))

if score > 100 or score < 0:
    print("0~100까지의 점수를 입력하세요!")
elif score >= 90:
    if score == 100:
        print("A+")
    else:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    if score == 0:
        print("(빵점)", end="")
    else:
        print("F")
'''


# 조건문 연습
'''
    1. 나이를 입력 받고 아래 조건에 맞게 출력
        7세 이하 : 아동입니다.
        8세~19세 : 청소년입니다.
        20세~64세 : 성인입니다.
        65세 이상 : 노인입니다.
    [출력결과]
    나이 입력 : 15
    청소년입니다.
'''
"""
age = int(input("나이 입력 :"))

if age < 0:
    print("잘못 입력하셨습니다.")
elif age <= 7:
    print("아동입니다.")
elif age <= 19:
    print("청소년입니다.")
elif age <= 64:
    print("성인입니다.")
else:
    print("노인입니다.")
"""

'''
    2. 주민등록번호 남/녀 판별기
        주민등록번호를 010101-3456789 형태로 입력 받고,
        7번째 숫자에 따라 "남자" 또는 "여자" 출력
            9, 1, 3, 5, 7 : 남자
            0, 2, 4, 6, 8 : 여자

    [출력결과]
    주민등록번호 입력 : 010101-3456789
    남자

        >> 입력받은 주민등록번호를 바로 정수로 변환하면 안 됨...
'''
"""
num1 = input("주민등록번호 입력 :")
num2 = int(num1[7])
"""
'''
if num2 in [1, 3, 5, 7, 9]:
    print("남자")
else:
    print("여자")
'''
"""
if num2 % 2 == 0:
    print("여자")
else:
    print("남자")
"""
'''
    3. 3개 과목의 점수를 입력 받고, 평균 점수에 따라 합격/불합격 출력
        - 평균 60점 이상 합격
        - 평균 점수는 소수점 첫 번째 자리까지만 출력
        - 합격일 때, 65점 미만이면 "턱걸이하셨네요~~!"를 추가로 출력        

    [출력결과]
    세 과목 점수 입력 : 60 60 61
    당신은 60.3점으로 합격입니다.
    턱걸이하셨네요~~!
'''
"""
num1, num2, num3 = map(int, input("세 과목 점수 입력 :").split())
num4 = num1+num2+num3
num5 = num4 / 3
"""
'''
if num5 < 0:
    print("다시 입력해주세요.")
elif num5 >= 60:
    if num5 < 65:
        print("턱걸이하셨네요~~!")
    else:
        print("당신은 {:.1f}점으로 합격입니다.".format(num5)")
else:
    print("재도전하세요.")
'''
# 답
'''
if avg >= 60:
    print(f"당신은 {avg:.1f}점으로 합격입니다.")

    if avg < 65:
        print("턱걸이하셨네요~~~!")

else:
    print("불합격입니다!")
'''




'''
    4. 세가지 수를 입력 받아 가장 큰 수를 출력하기 

    [출력결과]
    세 수 입력 : 20 34 32
    제일 큰 수 : 34
'''
# 답
'''
num1, num2, num3 = map(int, input("세 수 입력:").split())

result = 0

if num1 > num2:
    if num1 > num3:
        result = num1
    else:
        result = num3
elif num2 > num3:
    result = num2
else:
    result = num3

print(f"제일 큰 수 : {result}")
'''

'''
    5. 똑똑한 계산기
        - 2개의 숫자와 연산할 기호를 입력 받고 결과를 출력하기
            (1) 계산할 2개의 숫자를 입력 받기
            (2) 연산할 기호를 입력 받기
            (3) 연산 기호에 맞는 결과를 출력

     [출력결과1]
     2개의 숫자를 입력하세요 : 10 3
     연산할 기호를 입력하세요(+,-,*,/) : +
     결과 : 10 + 3 = 3
     
     [출력결과2]
     2개의 숫자를 입력하세요 : 10 3
     연산할 기호를 입력하세요(+,-,*,/) : /
     결과 : 10 / 3 = 3.3
'''
"""
num1, num2 = map(int, input("2개의 숫자를 입력하세요 :").split())
calc = input("연산할 기호를 입력하세요(+,-,*,/) :")

if calc == "+":
    print(f"{num1} + {num2} = {num1 + num2}")

elif calc == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
    
elif calc == "*":
    print(f"{num1} * {num2} = {num1 * num2}")

elif calc == "/":
    print(f"{num1} / {num2} = {num1 / num2:.1f}")

"""

