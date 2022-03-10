import re
ff = open("pi-billion.txt","r")
ff_content = ff.read()
n = 0

# 00000000 - 99999999  OK
obj_str = "00000000"
for i in re.finditer(obj_str, ff_content):
    n = n + 1
    print(n, i.start()-1, i.group())
ff.close()
