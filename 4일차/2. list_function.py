# list_function.py

'''
    리스트 관련 함수
        리스트. 함수() 형태로 사용
            > 문자열과 다르게 리스트는 수정이 되는 자료형이라
              리스트 자체가 수정된다.
'''

# append(value) : 리스트 가장 뒤에 value를 추가
a = [1]
a. append("!")
print("a =", a)
# 하나의 값만 추가 가능
a.append([1, 2, 3])
print("a =", a)
print()

# sort() : 리스트 정렬하기 (숫자, 알파벳, 한글 등)
a = [2, 4, 1 ,3]
a.sort()
print("a =", a) # 오름차순
a.sort(reverse=True) # 내림차순
print("a =", a)
print()

# reverse() : 리스트 뒤집기 (정렬x)
a = ["B", "C", "A", "D"]
a.reverse()
print("a =", a)
print()

# index(value) : 리스트에서 value를 찾고, 그 위치를 반환
a = [1, "A", 2, "B"]

print(a.index("B"))
print("이거이거"*2)

# insert(index, value) : 지정한 위치(index)에 값(value) 삽입
a = ["A", "B", 1, 2]
a.insert(2, "C")
print("a =", a)
print()

# remove(value) : 리스트에서 처음 찾은 값 제거
a = ["A", "B", "C", "A"]
a.remove("A")
print("a =", a)
# a.remove("X")
print()

#count(value) : 리스트에 존재하는 value의 개수 반환
a = [1,2,3,2,3,2,1,1,1,2,3,3,3,2,2,2]
print(a.count(3))
print()

# pop(index) : 리스트에서 index번째 값을 '뽑아낸다'
#   > 뽑아낸 값을 반환 해준다.
#   > 뽑아낸 값은 리스트에서 제거된다.

a = ["A", "B", "C", "D"]
print(a.pop(2))
print("a =", a)
print(a.pop()) # 기본이 맨 뒤
print("a =", a)
print()

# len() : 요소의 개수를 구하는 함수
a = [1, 2, 3, 4]
b = "abcdefg"
c = 1111

print(len(a))
print(len(b))
# print(len(c)) # 값이 여러 개 존재하는 자료형만 len을 사용할 수 있다.
print()

#copy() : 모든 값들을 복제하여 새로운 리스트를 생성
a = [1, 2, 3, 4] 
b = a.copy()
c = a

print("기존 a :", a) # 리스트는 메모리에 저장됨 그리고 a는 메모리에 저장된 리스트를 가리킴 b는 그 행위 자체를 복사 c는 a랑 똑같이 가리킴
print("복제 b :", b)
print("대입 c :", c)


a[0] = -20
print()
print("기존 a :", a)
print("복제 b :", b)
print("대입 c :", c)
print()

# clear() : 리스트의 모든 요소 제거
a.clear()
print(a)
print(c)

# list의 요소들이 '문자열'로만 이루어진 경우
# 문자열 관련 함수 중에서 join()을 이용하여 하나의 문자열을 만들 수 있다.

list1 = ["대","한", "민", "국"] # 숫자가 들어가면 못씀
print("".join(list1))
print()

'''
    1. 에이프릴, 폴킴, 방탄소년단, 에이핑크, 장범준 을 리스트로 만든 후
       엠씨더맥스를 마지막에 추가하라.

    2. 만들어진 리스트를 오름차순으로 정렬하라.

    3. 만들어진 리스트의 3번째 요소를 김필로 변경하라.

    4. 만들어진 리스트를 뒤집어라.
    
'''
singer = ["에이프릴", "폴킴", "방탄소년단", "에이핑크", "장범준"]
print(f"가수 리스트 : {singer}")
singer.append("엠씨더맥스")
print(f"가수 리스트 : {singer}")
singer.sort()
print(f"가수 리스트 : {singer}")

singer[2] = "김필"
print(f"가수 리스트 : {singer}")

singer.reverse()
print(f"가수 리스트 : {singer}")
print()

'''
    리스트 활용 연습하기
      my_list를 이용하여 "안녕하세요!" 문자열을 만들고 출력하기
      join() 함수 활용
    my_list = [ "!", "요", "세", "요", "하", "녕", "안" ]
    
'''

my_list = [ "!", "요", "세", "요", "하", "녕", "안" ]

my_list.reverse()
print(my_list)
my_list.remove("요")
print(my_list)
print("".join(my_list))










