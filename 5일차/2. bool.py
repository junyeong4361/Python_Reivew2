# bool.py

'''
    [7. bool 자료형]
        - 참(True)과 거짓(False)을 포현하는 자료형

        - 자료형의 값에 따른 참과 거짓

            값         True/False
            ---------------------------
            0               False
            1               True
            -10             True
            "abc"           True
            ""              False
            []              False
            ()              False
            None            False

            거짓인 경우
                1. 요소가 없다. (문자열, 리스트, 튜플 등)
                2. 숫자가 0이다.
                3. None 일 때 (값이 없다는걸 의미하는 값)

            
'''

#bool 자료형

# bool(value) : True/False

print(bool(0))
print(bool(1))
print(bool(-10))
print(bool("hahaha"))
print(bool(0.0185))
print(bool())
print(bool(0.0))

'''
    숫자 : 그냥 쓰면 된다.
    문자열 : 따옴표로 묶는다.
    리스트 : []
    튜플 : ()
    딕셔너리 : {k:v}
    집합 : {}
    bool : True/False
'''



















