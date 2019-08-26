import re 

p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")

print(m)

p2 = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m2 = p.search("park 010-1234-1234")

print(m2.group(0))   # 문자열 전체
# print(m2.group(1))   # 매칭된 문자열 첫번째 그룹

p3 = re.compile(r'(\b\w+)\s+\1')         # 메타 문자 \1 이 앞에 그룹을 나타낸다. 같은 패턴이 두번 반복 # \b 는 단어 구분자
m3 = p3.search('Paris in the the spring')
print(m3)