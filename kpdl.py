import numpy as np
import pandas as pd
import bin as b
from prettytable import PrettyTable

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# round
r = 2

BIN_TYPE = {"EQUAL_WIDTH": 0, "EQUAL_DEPTH": 1}


def mr(number):
    return round(number, r)


class KPDL:

    def __init__(self):
        self.x = []

    def __init__(self, x=[], bin=3, name="name"):
        self.x = x
        self.x_sz = len(self.x)
        self.x_sorted = sorted(self.x)
        self.x_avg = mr(np.average(self.x))
        self.name = name
        self.bin = bin
        self.max = max(self.x)
        self.min = min(self.x)

    def showSorted(self):
        if len(self.x) > 0:
            print("+) sorted:", self.x_sorted)

    def avg(self):
        if len(self.x) > 0:
            avg = np.average(self.x)
            print("+) avg:", round(avg, r))

    def median(self):
        l = len(self.x)
        x = sorted(self.x)
        if l > 0:
            avg = np.median(self.x)
            if l % 2:
                print("+) median:", round(avg, r))
            else:
                print("+) median:({0} + {1}) / 2 = {2}".format(x[int(l / 2) - 1], x[int(l / 2)],
                                                               round(avg, r)))

    def readExcel(self):
        return

    def mode(self):
        l = len(self.x)

        if l > 0:
            x = np.array(self.x)
            unique, counts = np.unique(x, return_counts=True)
            res = np.asarray((unique, counts)).T
            m = max([i[1] for i in res])

            def _func(x):
                return x[1] == m

            print("+) mode: rỗng") if l == len(res) else print("+) mode:",
                                                               [str(x[0]) + " tần xuất:" + str(x[1]) for x
                                                                in
                                                                list(filter(_func, res))])

    def box_plot(self):
        x = sorted(self.x)
        _max = mr(max(x))
        _min = mr(min(x))
        _n = len(x)
        mid = int(_n / 2) + 1 if _n % 2 else int(_n / 2)
        Q1 = mr(np.median(x[:int(_n / 2)]))
        Q2 = mr(np.median(x))
        Q3 = mr(np.median(x[mid:]))
        IQR = mr(Q3 - Q1)
        minimum = mr(Q1 - 1.5 * IQR)
        maximum = mr(Q3 + 1.5 * IQR)
        print("+) min = {0}, max = {1}, n = {2}".format(_min, _max, _n))
        print("+) Q1 = {0}, Q2 = {1}, Q3 = {2}".format(Q1, Q2, Q3))
        print(
            "+) Minimun = Q1-1.5*IQR = {Q1}-1.5*{IQR} = {minimum}, Maximun = Q3+ 1.5*IQR = {Q3}+1.5*{IQR} = {maximum}".format(
                minimum=minimum, maximum=maximum, Q1=Q1, Q3=Q3, IQR=IQR))
        print("+) Biểu đồ boxplot")
        ngoai_lai = [i if i < _min or i > _max else None for i in self.x]

        def _func(x):
            return x != None

        ngoai_lai = list(filter(_func, ngoai_lai))
        if len(ngoai_lai) == 0:
            print("+) Không có ngoại lai")
        else:
            print("Ngoại lai:", ngoai_lai)

        # np.random.seed(10)
        # data = np.random.normal(100, 20, 200)
        #
        # fig = plt.figure(figsize=(10, 7))
        #
        # # Creating plot
        # plt.boxplot(data)
        # img = mpimg.imread('boxplot.png')
        # imgplot = plt.imshow(img)
        # plt.show()

        # show plot
        # plt.show()

    def z_score(self):
        print("Ta có:")
        self.avg()
        nuy = ((sum([mr(i ** 2) for i in self.x]) / self.x_sz) - mr(np.average(self.x)) ** 2)
        nuy = mr(nuy)
        print("σ^2 = 1/n * Tổng_sigma(1 đến n, xi^2) - avg^2 = ", nuy)
        print("=> σ = ", np.sqrt(nuy))
        print("Ta có : v1' = (v1 - avg) / σ = {0}".format(mr((self.x_sorted[0] - self.x_avg) / np.sqrt(nuy))))
        x_std = [mr((i - self.x_avg) / mr(np.sqrt(nuy))) for i in self.x_sorted]
        cols = ["T"] + [str(i) for i in range(0, 12)]
        tb =  PrettyTable(cols)
        tb.add_row(["v"] + self.x_sorted)
        tb.add_row(["v'"] + x_std)
        print(tb)

        # df = pd.DataFrame(d, columns=[str(i) for i in range(-1, self.x_sz)])
        # print(df)
        # print("arr:", self.x_sorted)
        # print("v':", x_std)
        # print([str(i) for i in range(-1, self.x_sz)])

        # print(["v"]+self.x_sorted)
        # print(["v'"] + x_std)
        # ptb = PrettyTable()
        # ptb.field_names = ["v"]+[str(i) for i in self.x_sorted]
        # ptb.add_row(["v'"] + x_std)
        # print(ptb)

    def bin_smoothing(selfs):
        print("equal frequency binning(depth)".upper())
        b.equifreq(selfs.x, 3)

        print("\n\nequal width binning(width)".upper())
        b.equiwidth(selfs.x, 3)

    def run(self):
        print(str("-" * 50) + "begin " + self.name + str("-" * 50))
        print("\na)")
        self.showSorted()
        self.avg()
        self.median()
        self.mode()
        print("\nb) Vẽ biểu đồ boxplot:")
        self.box_plot()
        print("\nc) Chuẩn z-scrore:")
        self.z_score()
        print("\nc) Bin:")
        self.bin_smoothing()
        print("\ne) Mối tương quan giữa x và y(xem ảnh tuong_quan.jpg):")
        print(str("-" * 50) + "end " + self.name + str("-" * 50))


def includes(srcs=[], vals=[]):
    for val in vals:
        if val not in srcs:
            return False
    return True


class Apriori:
    def __init__(self, id=[], items=[]):
        self.id = id
        self.items = items
        self.sz_id = len(self.id)
        self.sz_items = len(self.items)
