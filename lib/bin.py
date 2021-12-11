import numpy as np
import copy


def smoothing(res):
    print("*smoothing:(làm trơn)")
    print("-mean:(trung bình)")
    res_1 = copy.copy(res)
    for index, bin in enumerate(res_1):
        avg = np.average(np.array(bin))
        avg = round(avg, 2)
        res_1[index] = [avg] * len(res_1[index])
    for index, bin in enumerate(res_1):
        print("bin{0}={1}".format(index + 1, bin))
    print("-median:(trung vị)")
    res_2 = copy.copy(res)
    for index, bin in enumerate(res_2):
        median = np.median(np.array(bin))
        res_2[index] = [median] * len(res_2[index])
    for index, bin in enumerate(res_2):
        print("bin{0}={1}".format(index + 1, bin))
    print("-boundaries:(biên)")
    res_3 = copy.copy(res)

    for index, bin in enumerate(res_3):
        ma = np.max(bin)
        mi = np.min(bin)
        for index2, bin2 in enumerate(bin):
            if bin2 - mi < ma - bin2:
                bin[index2] = mi
            elif bin2 - mi > ma - bin2:
                bin[index2] = ma
            else:
                bin[index2] = mi
    for index, bin in enumerate(res_3):
        print("bin{0}={1}".format(index + 1, bin))


def equifreq(arr1, m):
    a = len(arr1)
    n = int(a / m)
    res = []
    for i in range(0, m):
        arr = []
        for j in range(i * n, (i + 1) * n):
            if j >= a:
                break
            arr = arr + [arr1[j]]
        res.append(arr)
    for index, bin in enumerate(res):
        print("bin{0}={1}".format(index + 1, bin))
    smoothing(res)


# equal width
def equiwidth(arr1, m):
    a = len(arr1)
    w = int((max(arr1) - min(arr1)) / m)
    min1 = min(arr1)
    arr = []
    for i in range(0, m + 1):
        arr = arr + [min1 + w * i]
    arri = []

    for i in range(0, m):
        temp = []
        for j in arr1:
            if j >= arr[i] and j <= arr[i + 1]:
                temp += [j]
        arri += [temp]
    for index, bin in enumerate(arri):
        print("bin{0}={1}".format(index + 1, bin))

    smoothing(arri)


# # data to be binned
# data = [5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215]
#
# # no of bins
# m = 3
#
# print("equal frequency binning(depth)")
# equifreq(data, m)
#
# print("\n\nequal width binning(width)")
# equiwidth(data, 3)