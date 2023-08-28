# 정규 표현식

"""
* 정규 표현식 : 복잡한 문자열을 처리할 때 사용하는 기법, 파이썬 말고도 모든 곳에서 사용함

# 정규 표현식이 필요한 이유
ex) 주민번호 뒷자리 7자리를 *로 변환하기
"""

data = """
park 800905-1049118
kim 700905-1059919
"""

result = []
for line in data.split('\n'):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))

# 정규표현식을 사용한 더 간략한 코드
import re

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))