import re

p = re.compile(r'\bclass\b')
p2 = re.compile(r'\Bclass\B')

m = p.search('no class at all')
m2 = p.search('the declassified algorithm')
print(m)
print(m2)

m3 = p2.search('no class at all')
m4 = p2.search('the declassified algorithm')
print(m3)
print(m4)

# \b 메타 문자를 사용할 때 주의해야 할 점이 있다. \b는 파이썬 리터럴 규칙에 의하면 백스페이스(BackSpace)를 의미하므로 백스페이스가 
# 아닌 단어 구분자임을 알려 주기 위해 r'\bclass\b'처럼 Raw string임을 알려주는 기호 r을 반드시 붙여 주어야 한다.

