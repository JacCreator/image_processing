import numpy as np


def histogram(img):
    h = np.zeros(256, dtype=int)
    for row in img:
        for pixel in row:
            h[pixel] += 1
    return h


''' 
    Wersja algorytmu 2
    def D(k, s):
        sumPo = 0
        sumQo = 0
        sumPb = 0
        sumQb = 0

        qOArray = arr.array('f', [0])
        qBArray = arr.array('f', [0])

        l = 1
        #normalizacja qO
        for i in range(1, s):
            qOArray.append(qO(l, s))
            l += 1
        qOMean = np.mean(qOArray)
        qODev = np.std(qOArray)
        # normalizacja qB
        for i in range(1, s):
            qBArray.append(qO(l, s))
            l += 1
        qBMean = np.mean(qOArray)
        qBDev = np.std(qOArray)

        for i in range(1, s):
            a = (qO(k, i) - qOArray) / qODev
            b = pO(k, i)
        if a == 0:
            a = 1e-2
        if b == 0:
            b = 1e-2
        sumPo += b * np.log10(b / a)
        sumQo += a * np.log10(a / b)
        for j in range(s + 1, L):
        c = pB(k, j)
        d = (qB(j) - qBMean) / qBDev
        if c == 0:
            c = 1e-2
        if d == 0:
            d = 1e-2
        sumPb += c * np.log10(c / d)
        sumQb += d * np.log10(d / c)

    return sumPo + sumPb + sumQb + sumQo

'''


def algorithm1(img):
    # zmienne globalne
    global h
    global L

    h = histogram(img)
    mindiv = int(np.argmax(h))
    L = int(len(h))

    k = 1
    # drukowanie hogramu
    print('Histogram' + str(h))

    for s in range(2, L):
        print(format(s / L * 100, '.2f') + str('%'))
        if mindiv > D(k, s):
            mindiv = D(k, s)
        k += 1
    # wydrukowanie wyniku
    print(mindiv)
    return mindiv


def factorial(number):  # funckja silnia
    s = 1
    for i in range(2, number + 1):
        s *= i
    return s


def pO(k, s):
    Ps = 0.1
    for i in range(1, s):
        Ps += h[i]
    return float((h[k]) / (Ps))


def pB(k, s):
    # MN: 12*22 = 256
    Ps = 0.1
    for i in range(s + 1, L):
        Ps += h[i]
    return float(h[k] / (256 - Ps))


def lambdaO(s):
    sum1 = 0
    sum2 = 1e-5
    for i in range(1, s):
        sum1 += i * h[i]
        sum2 += h[i]
    return float(sum1 / sum2)


def lambdaB(s):
    sum1 = 0
    sum2 = 0.1
    for i in range(s + 1, L):
        sum1 += i * h[i]
        sum2 += h[i]

    return float(sum1 / sum2)


def qO(k, s):
    if k > 170:
        k = 170
    lamO = lambdaO(s)
    x = np.mean([1, float(np.exp(-lamO) * lambdaO(k) / factorial(k))])
    return x


def qB(s):
    if s + 1 > 168:
        s = 168
    lamB = lambdaB(L)
    x = np.mean([1, float(np.exp(-lamB) * lambdaB(s + 1) / factorial(s + 1))])
    return x


def D(k, s):
    sumPo = 0
    sumQo = 0
    sumPb = 0
    sumQb = 0

    for i in range(1, s):
        a = qO(k, i)
        b = pO(k, i)
        if a == 0:
            a = 1e-10
        if b == 0:
            b = 1e-10
        sumPo += b * np.log10(b / a)
        sumQo += a * np.log10(a / b)
    for j in range(s + 1, L):
        c = pB(k, j)
        d = qB(j)
        if c == 0:
            c = 1e-10
        if d == 0:
            d = 1e-10
        sumPb += c * np.log10(c / d)
        sumQb += d * np.log10(d / c)

    return float(sumPo + sumPb + sumQb + sumQo)


if __name__ == '__main__':
    print("Uruchom plik imageProcessing.py")