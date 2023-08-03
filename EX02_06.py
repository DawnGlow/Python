# 집합 자료형

"""
# 집합 자료형은 어떻게 만들까?
- 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형
- set 키워드를 통해 만든다
s1 = set([1,2,3])
s1
res : {1, 2, 3}
s2 = set("Hello")
s2
res : {'e', 'H', 'l', 'o'} # ???

# 집합 자료형의 특징
- 중복을 허용하지 않는다.
- 순서가 없다(Unordered)
- 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다.
- 딕셔너리 역시 순서가 없어 인덱싱을 지원하지 않음.
- 인덱싱으로 접근하고 싶으면 리스트로 형변환하자.

# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

* 교집합
s1 & s2
res : {4, 5, 6}

s1.intersection(s2)
res : {4, 5, 6}

s2.intersection(s1)
res : {4, 5, 6}

* 합집합
s1 | s2
res : {1, 2, 3, 4, 5, 6, 7, 8. 9}

s1.union(s2)
res : {1, 2, 3, 4, 5, 6, 7, 8. 9}

* 차집합
s1 - s2
res : {1, 2, 3}

s1.difference(s2)
res : {1, 2, 3}

s2 - s1
res : {8, 9, 7}

s2.difference(s1)
res : {8, 9, 7}

# 집합 자료형 관련 함수

* 값 1개 추가하기(add 함수)
s1 = set([1, 2, 3])
s1.add(4)
s1
res : {1, 2, 3, 4}

* 값 여러개 추가하기(update 함수)
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
s1
res : {1, 2, 3, 4, 5, 6}

* 특정 값 제거하기(remove 함수)
s1 = set([1, 2, 3])
s1.remove(2)
s1
res : {1, 3}
"""