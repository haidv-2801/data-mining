import numpy as np

from lib import kpdl

a = [4.9, 4.6, 5.7, 5.4, 7, 4.5, 5.5, 6.5, 6.1, 5.3, 5, 5.1]
b = [3, 3.1, 4.4, 3.9, 3.2, 2.3, 3.5, 2.8, 2.8, 3.7, 3.3, 3.5]

# không truyền bin thì mặc định số thùng là 3
l = kpdl.KPDL(x=a, name="X", bin=4)
l.run()

l = kpdl.KPDL(x=b, name="Y", bin=4)
l.run()
