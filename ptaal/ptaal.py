import re

pattern = re.compile(r'(ij|[aeoui]+)p\1', re.IGNORECASE)
for k in range(int(input())):
    print(pattern.sub(r'\1', input()))