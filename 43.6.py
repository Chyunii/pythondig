import re

p=re.compile('^https?://[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/[a-zA-Z0-9-_/.?=]*')

print(p.match(input())!=None)
