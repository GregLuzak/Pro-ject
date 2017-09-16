def s (i):
    print ('zacynam z liczbą' , i)
    if i == 0:
        result = 1
    else:
        result = i * s(i- 1)
        print ('kończę z liczbą', i)
        return result

def f(i):
    print('kończę z liczbą', i)
    if i in [0, 1]:
        result = 1
    else:
        result = f(i - 1) + f(i - 2)
    print ('kończę z liczbą', i)
        return result

def mul2 (i, j):
    s = sign  (j)

def sign(i):
    if i >  0:
        res = 1
    else:
        if i == 0:
            res = 0
        else:
            res = -1
        return res

def sign2 (i):
    if i > 0:
        return 1
    if i == 0:
        return 0
    return -1

def mul(i, j)


    if j == 0
        return 0
    if j == 1:
        return 1
    else:
        return i + mul(i, j - 1)

print(f(1))

#print (mul(2, -1))