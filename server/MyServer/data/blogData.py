import sys
import os
pwd = os.path.dirname(os.path.realpath(__file__))
print(pwd)
sys.path.append(pwd+'/../')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyServer.settings')

import django
django.setup()

from apps.blogs.models import Blog, Category
from apps.users.models import MyUser
from apps.blogs.models import Category
import json
import os
import time

for file in os.listdir('.'):
    print(file)

with open('category.json', 'r', encoding='utf8') as f:
    for line in f.readlines():
        p = json.loads(line)
        #print(p['name'][0], p['categoryId'], p['value'][0])
        c=Category(name=p['name'][0], categoryId=p['categoryId'], value= p['value'][0])
        c.save()
        
with open('blog.txt', 'r', encoding='utf8') as f:
     for line in f.readlines():
        p = json.loads(line)
        now = time.time()
        title = p['title']
        user = MyUser.objects.get(username='pan')
        blogId = str(hash(str(now) + title)).replace('-', '')
        content = p['content']
        category = Category.objects.get(categoryId=p['category'])
        blogId = str(hash(str(now) + title)).replace('-', '')
        link = "/blog/%s" % (blogId)
        print(category)
        descript = p['summary'][:50]
        blog = Blog(title=title, content=content, category=category,
                    descript=descript, authorId=user, blogId=blogId, link=link)
        blog.save()         