import numpy as np

from lib import kpdl

a = [9.1, 4.5, 5.3, 6.7, 6.5, 7.0, 6.0, 5.5, 7.0, 7.0, 8.5, 1000]
b = [8.5, 5.5, 6.0, 7.5, 8.5, 6.0, 6.5, 6.8, 9.0, 7.2, 8.0, 8.5]

# không truyền bin thì mặc định số thùng là 3
l = kpdl.KPDL(x=a, name="X", bin=3)
l.run()

# l = k.KPDL(x=b, name="Y", bin=3)
# l.run()

