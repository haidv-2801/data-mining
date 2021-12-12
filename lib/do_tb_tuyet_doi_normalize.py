import numpy as np
from prettytable import PrettyTable

# sửa các tham số ở đây
x = [200, 300, 400, 600, 1000]
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
