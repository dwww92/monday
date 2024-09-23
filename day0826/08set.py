# 08set.py
# 추가, 수정, 삭제 불가 ===> 튜플데이터
# 튜플과 리스트를 셋에 그대로 넣을 수 있다.

# 셋 set {} 
# 순서 X, 중복 X
# append(),insert()==add()대체
# 전체삭제 clear()
 
wish = { }
# 선언하면 set아니라 dict로 인식함
# 실행하면 에러 발생

print(wish)

wish.add('엘쥐')
wish.add('kt')
wish.add(37.081)
wish.add('엘쥐')
wish.add('엘쥐')

print(wish)

n_tuple = (1,2,3,4)

n_list = [5,6,7,8]