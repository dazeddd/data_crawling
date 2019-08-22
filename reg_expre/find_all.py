import re

p = re.compile('[a-z]+', re.IGNORECASE)    # 패턴은 정규식을 컴파일해서

result = p.findall("I am a amazing person")
print(result)                              # 리스트를 반환

result2 = p.finditer("You are idiot")
print(result2)

for s in result2:
    print(s)


