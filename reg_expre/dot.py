import re

# "a + 모든문자 + b"
p = re.compile('a.b')

# "a + Dot(.)문자 + b"
p = re.compile("a[.]b")