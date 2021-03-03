# 입력 연습

'''
    1. 사각형 면적 구하기
        가로,세로를 입력 받고 면적을 출력

    [출력결과]
    가로, 세로 입력 : 4 5
    면적은 20입니다.
'''

width, height = map(int, input("가로, 세로 입력 : ").split())
print( "면적은 {}입니다.".format(width * height) )

