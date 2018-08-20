
import json

with open('blog.txt', 'r', encoding='utf8') as f:
    print('open file')
    for line in f.readlines():
        p = json.loads(line)
        print(p['title'])