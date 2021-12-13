import numpy as np
from prettytable import PrettyTable

# sửa các tham số ở đây
# x = [4.9, 4.6, 5.7, 5.4, 7, 4.5, 5.5, 6.5, 6.1, 5.3, 5, 5.1]
x = [3, 3.1, 4.4, 3.9, 3.2, 2.3, 3.5, 2.8, 2.8, 3.7, 3.3, 3.5]
# end

mean = np.average(x)
doTBtuyetDoi = (1 / len(x)) * sum([np.fabs(item - mean) for item in x])

# tạo bảng
cols = ["T"] + [str(i + 1) for i in range(len(x))]
tb = PrettyTable(cols)

if __name__ == '__main__':
    print("n: ", len(x))
    print("mean: ", mean)
    print("S = 1/n * (tổng_sigma(từ 1->n,của |xi-mean|)): ", doTBtuyetDoi)
    print("--trình bày trước 1 phép tính--")
    print("V'1 = (V1 - mean)/doTBtuyetDoi = ...")
    rows = [["Vi"] + x,
            ["Vi'"] + [(item - mean) / doTBtuyetDoi for item in x]]
    tb.add_rows(rows)
    print(tb)
