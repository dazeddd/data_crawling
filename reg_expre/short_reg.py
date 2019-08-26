import re

p = re.compile('[a-z]+')
m = p.match("python")


m2 = re.match('[a-z]+', "python")    #위의 식을 축약한 형태

print(m)
print(m2)