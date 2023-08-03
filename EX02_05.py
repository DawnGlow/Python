# 딕셔너리 자료형(Dictionary)

"""
# 딕셔너리?
- 대응 관계를 나타내는 자료형
- 연관 배열 또는 해시 라고 함
- 'people' 에 '사람', 'baseball' 에 '야구'
- key 와 value를 한쌍으로 갖는 자료형
- key를 통해 value를 얻는다.

# 딕셔너리 만드는 법
{Key1:Value1, Key2:Value2, Key3:Value3, ...}
ex)
dic = {'name':'pey', 'phone':'01199993323', 'birth':'1118'}
a = {1: 'hi'}
a = {'a': [1,2,3]}

# 딕셔너리 쌍 추가, 삭제
* 딕셔너리 쌍 추가
a = {1: 'a'}
a[2] = 'b' # 이름[key] = value
a
res : {1: 'a', 2: 'b'}
a['name'] = 'pey'
a
res : {1: 'a', 2: 'b', 'name': 'pey'}
a[3] = [1, 2, 3]
a
res : {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

* 딕셔너리 요소 삭제
a = {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}
del a[1] # key가 1 인 key:value 삭제
a
res : {2: 'b', 'name': 'pey', 3: [1, 2, 3]}


# 딕셔너리를 사용하는 방법

* 어떤 용도로 사용?
사람과 특기를 대응, 이런 관계에 사용

* 딕셔너리 Key를 사용해 Value 얻기
grade = {'pey': 10, 'julliet': 99}
grade['pey']
res : 10
grade['julliet']
res : 99

* 딕셔너리를 만들 때 주의사항
- 딕셔너리에서 Key는 고유한 값이므로 중복되는 Key를 설정하면, 하나를 제외한 나머지가 무시된다. ex)
a = {1: 'a', 1: 'b'}
a
res : {1: 'b'}

- Key에는 리스트를 사용할 수 없다(에러 발생). 하지만 튜플은 사용할 수 있다. (튜플은 변하지 않는 값이기 때문)
- 딕셔너리 key에 딕셔너리는 당연히 사용하지 못한다.
- Value는 전혀 상관없다.


# 딕셔너리 관련 함수

* Key 객체 만들기(keys 함수) : 이름.keys()
a = {'name': 'pey', 'phone': '01034242424', 'birth': '1118'}
a.keys() // dicts_keys 객체를 리턴한다.
res : dict_keys(['name', 'phone', 'birth'])

- Python 3.0 이전에는 a.keys() 리턴값이 리스트였지만, 3.0 이후에는 메모리 낭비를 줄이기 위해 dicts_keys 객체를 리턴함.
- list가 필요하면, list(a.keys()) 사용하면 됨.
- dict_keys, dict_values, dict_items 등은 리스트로 변환하지 않아도 iterate(반복) 구문 실행 가능하다.
ex) for문 사용
for k in a.keys():
    print(k)

res:
name
phone
birth

- 리스트 고유의 append, insert, pop, remove, sort함수는 사용할 수 없다.
list(a.keys())
res : ['name', 'phone', 'birth']

* Value 객체(리스트) 만들기 (values 함수)
a.values()
res : dict_values(['pey', '01034242424', '1118'])

* Key, Value 쌍 객체(리스트) 얻기(items 함수)
a.items() # Key와 Value 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다
res : dict_items([('name', 'pey'), ('phone', '01034242424'), ('birth', '1118')])

* Key, Value 쌍 모두 지우기(clear 함수)
a.clear() # 모든 요소 삭제
a
res : {}

* Key로 Value 얻기(get 함수)
a = {'name': 'pey', 'phone': '01034242424', 'birth': '1118'}
a.get('name') # a['name'] 과 같은 결과
res : 'pey'

- a['nokey']는 오류를 발생시키지만, a.get('nokey')는 None을 돌려준다.

* get함수 default 값 셋팅 (찾으려는 key가 없는 경우)
- a.get(x, '디폴트값') 사용
a.get('foo', 'bar') # 딕셔너리에 'foo'라는 값이 없어서 'bar'를 돌려준다.

* 해당 Key가 딕셔너리에 있는지 조사하기(in)
a = {'name': 'pey', 'phone': '01034242424', 'birth': '1118'}
'name' in a
res : True
'email' in a
res : False
"""