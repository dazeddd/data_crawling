import re

p = re.compile('(blue|white|red)')
s = p.sub('colour', 'blue socks and red shoes')
s2 = p.sub('colour', 'blue socks and red shoes', count=1)

print(s)
print(s2)    # 앞에서부터 한번한 substitute 해준다 (count=1)

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")

print(p.sub("\g<2> \g<1>", "park 010-1234-1234"))
print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))