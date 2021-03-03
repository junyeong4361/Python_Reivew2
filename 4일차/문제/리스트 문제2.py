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
















































