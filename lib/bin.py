import numpy as np
import copy


def smoothing(res):
    print("*smoothing:(làm trơn)")
    print("-mean:(trung bình)")
    res_1 = copy.copy(res)
    for index, bin in enumerate(res_1):
        avg = np.average(np.array(bin))
        avg = round(avg, 3)
        res_1[index] = [avg] * len(res_1[index])
    for index, bin in enumerate(res_1):
        print("bin{0}={1}".format(index + 1, bin))
    print("-median:(trung vị)")
    res_2 = copy.copy(res)
    for index, bin in enumerate(res_2):
        median = round(np.median(np.array(bin)),3)
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
    w = round((max(arr1) - min(arr1)) / m, 3)
    print("Width = ({0} - {1}) / {2} = {3}".upper().format(max(arr1), min(arr1), m, w))
    min1 = min(arr1)
    arr = []
    for i in range(0, m + 1):
        arr = arr + [round(min1 + w * i, 3)]

    arr[-1] = 10 ** 10
    arri = []

    for i in range(0, m):
        temp = []
        for j in arr1:
            if j >= arr[i] and j < arr[i + 1]:
                temp += [j]
        arri += [temp]

    for index, bin in enumerate(arri):
        print("bin{0}={1}".format(index + 1, bin))

    smoothing(arri)


# # data to be binned
# data = sorted([9.1, 4.5, 5.3, 6.7, 6.5, 7.0, 6.0, 5.5, 7.0, 7.0, 8.5, 8.6])
#
# # no of bins
# m = 3
#
# print("equal frequency binning(depth)")
# equifreq(data, m)
#
# print("\n\nequal width binning(width)")
# equiwidth(data, 3)
