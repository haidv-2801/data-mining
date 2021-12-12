import numpy as np

# không sort nhé các con vợ
a = [9.1, 4.5, 5.3, 6.7, 6.5, 7.0, 6.0, 5.5, 7.0, 7.0, 8.5, 8.6]
b = [8.5, 5.5, 6.0, 7.5, 8.5, 6.0, 6.5, 6.8, 9.0, 7.2, 8.0, 8.5]
r = 10 # làm tròn 10 chữ số sau dấu phẩy

n = len(a)
avg_a = round(np.average(a), r)
avg_b = round(np.average(b), r)
nuy_a = round(np.sqrt(1 / n * sum([i ** 2 for i in a]) - avg_a ** 2), r)
nuy_b = round(np.sqrt(1 / n * sum([i ** 2 for i in b]) - avg_b ** 2), r)

if __name__ == '__main__':
    print("n: ", n)
    print("a: ", a)
    print("b: ", b)
    print("mean_a: ", avg_a)
    print("mean_b: ", avg_b)
    print("nuy_a: ", nuy_a)
    print("nuy_b: ", nuy_b)
    res = (sum([round(a[i] * b[i], r) for i in range(0, n)]) - n * avg_b * avg_a) / (n * nuy_b * nuy_a)
    print("r_ab: ", round(res, r))
    if res < 0:
        print("Tương quan nghịch")
    elif res == 0:
        print("Không có tương quan")
    else:
        print("Tương quan thuận")
