import numpy as np
from prettytable import PrettyTable

# tìm j sao cho vi' = |vi / (10 ^ j)| có giá trị lớn nhất và < 1

# sửa các tham số ở đây
x = [200, 300, 400, 600, 1000]
# end

def s(a):
    a=max(a)
    b = 1
    i = 0
    while (a / b >= 1):
        i += 1
        b = b * 10
    return i


def decimal_scaling(x):
    print("xem lại cách trình bày trong ảnh decimal_scaling.jpg")
    print("Vi' = Vi / (10 ^ J) < 1")
    J = s(x)
    cols = ["T"] + [str(i + 1) for i in range(len(x))]
    tb = PrettyTable(cols)
    rows = []
    rows.append(["Vi"] + x)
    vi = [np.fabs(i / 10 ** J) for i in x]
    rows.append(["J"] + [J for i in x])
    rows.append(["Vi'"] + vi)
    tb.add_rows(rows)
    print(tb)


    print("Note: tự đối chiếu bảng tìm max(|V'i|) => J cần tìm")
    print("Không chép ở đây")


if __name__ == '__main__':
    decimal_scaling(x)
