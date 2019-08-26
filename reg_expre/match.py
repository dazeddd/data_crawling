import re

p = re.compile('[a-z]+')    # 패턴은 정규식을 컴파일해서

result = p.match('python')
result2 = p.match('3 python') # 처음 3이 정규식과 match 되지 않아서 None을 반환

result3 = p.search('3 python') # 문장 전체를 search 해서 match 되는 python 을 반환

print(result.group())
print(result.start())
print(result.end())
print(r)

print(result2)

print(result3)

