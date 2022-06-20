from datetime import datetime
import random
from hashlib import md5
import time

ar = []

def generate_uuid():
    now = datetime.now()

    hsh = "".join(str(random.random())+str(now)).encode('utf-8')
    md5val = md5(hsh).hexdigest()


    prefix = "".join(str(now.isocalendar().year)+str(now.isocalendar().week)).encode('utf-8')

    p1 = md5(prefix).hexdigest()[0:4]
    p2 = md5val[0:4]
    p3 = '-'+md5val[4:8]
    p4 = '-4'+md5val[8:11]
    p5 = '-'+md5val[11:15]
    p6 = '-'+md5val[15:27]

    uuid = "{}{}{}{}{}{}".format(p1,p2,p3,p4,p5,p6)

    return uuid


for x in range(0,50):
    uuid = generate_uuid()
    if uuid in ar:
        print("duplication")
        break
    else:
        print("new uuid key ",end="")
        print(uuid)
        ar.append(uuid)