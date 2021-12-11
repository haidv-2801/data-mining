import math as m
from prettytable import PrettyTable
import copy
import numpy as np
from collections import defaultdict

FILE_NAME = "lib/kmeans_data.txt"


def read_file(file):
    list = []
    with open(file) as f:
        for line in f:
            x, y = [float(x) for x in line.split()]
            list.append((x, y))
    return list


def dis(x, y):
    # mahatan
    return round(m.fabs(x[0] - y[0]) + m.fabs(x[1] - y[1]), 2)
    # khoang cach
    # return m.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


def equal(x, y):
    for index, i in enumerate(x):
        if x[index][0] != y[index][0] or x[index][1] != y[index][1]:
            return False
    return True


if __name__ == '__main__':

    n = ([(2, 10), (5, 8), (1, 2)])
    new_n = copy.copy(n)
    new_n.append((99999, 999999))
    _list = read_file(FILE_NAME)
    id = 1
    while 1:
        id += 1
        tb = PrettyTable()
        tb.field_names = ['STT'] + [str(str(i + 1) + '(' + str(x[0]) + ',' + str(x[1]) + ')') for i, x in
                                    enumerate(n)] + [
                             'Cụm']

        data = []
        for index_i, i in enumerate(_list):
            m_dis = 10 ** 10
            f = 1
            row = [index_i]
            for index_j, j in enumerate(n):
                dist = dis(i, j)
                row.append(round(dist, 2))
                if dist < m_dis:
                    m_dis = dist
                    f = index_j + 1
            row.append(f)
            data.append(row)
        tb.add_rows(data)

        new_data = [x[1:-1] for index, x in enumerate(data)]
        group = [x.pop() for index, x in enumerate(data)]
        new_table = defaultdict(list)
        n_1 = [[] for i in n]
        new_n = []
        for index, i in enumerate(_list):
            n_1[group[index] - 1].append(i)

        print(tb)
        for index, item in enumerate(n_1):
            if len(item) == 0:
                n_1[index].append(n[index])
            xs = round(np.average(np.array([x[0] for x in item])), 2)
            ys = round(np.average(np.array([x[1] for x in item])), 2)
            print(
                "Cụm {0}:{1}".format(index + 1, ','.join(
                    [str(str(index + 1) + '(' + str(x[0]) + ',' + str(x[1]) + ')') for index, x in
                     enumerate(item)])) + "=({0},{1})".format(xs, ys))
            new_n.append((xs, ys))
        # new_n = sorted(new_n)

        # print(new_n)
        if equal(n, new_n):
            break
        n = (new_n[:])
