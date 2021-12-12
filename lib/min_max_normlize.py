import numpy as np
from prettytable import PrettyTable

# sửa các tham số ở đây
x = [ 200, 300, 400, 600, 1000]
new_min = 0
new_max = 1

# tạo bảng
cols = ["T"] + [str(i + 1) for i in range(len(x))]
tb = PrettyTable(cols)

if __name__ == '__main__':
    old_min = min(x)
    old_max = max(x)
    print("Old max: ", old_max)
    print("Old min: ", old_min)
    print("--trình bày trước 1 phép tính--")
    print("V'1 = ((V1 - oldMin) / (oldMax - oldMin)) * (newMax - newMin) + newMin = {res}")
    rows = [["Vi"] + x,
            ["Vi'"] + [(item - old_min) / (old_max - old_min) * (new_max - new_min) + new_min for item in x]]
    tb.add_rows(rows)
    print(tb)
