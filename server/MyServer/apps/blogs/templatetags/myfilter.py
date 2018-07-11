from django import template

register = template.Library()
@register.filter(name='mytimesince')
def mytimesince(value):
    from datetime import datetime
    if isinstance(value, str):
        t = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    else:
        t = value
    n = datetime.now()
    dis = n-t
    if(dis.days <= 0):
        if dis.seconds > 3600:
            return '%d小时前' % (dis.seconds / 3600)
        elif dis.seconds > 60:
            return '%d分钟前' % (dis.seconds / 60)
        else:
            return '%d秒前' % (dis.seconds)
    else:
        if dis.days > 356:
            return '%d年前' % (dis.days / 356)
        elif(dis.days > 30):
            return '%d月前' % (dis.days/30)
        elif dis.days > 7:
            return '%d周前' % (dis.days / 7)
        else:
            return '%d天前' % (dis.days)