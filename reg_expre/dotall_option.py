# . 메타 문자는 줄바꿈 문자(\n)를 제외한 모든 문자와 매치되는 규칙이 있다.

import re

p = re.compile('a.b')
m = p.match('a\nb')
print(m)

p2 = re.compile('a.b', re.DOTALL)
m2 = p.match('a\nb')
print(m2)

