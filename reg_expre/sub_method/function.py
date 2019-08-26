import re

def hexrepl(match):              # match 되는 값을 인자로 받아서
    value = int(match.group())     
    return hex(value)

p = re.compile(r'\d+')
p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')