def kangaroo(x1, v1, x2, v2):
    for i in range(10000):
        if x1 == x2:
            return "YES"
        if (x1 < x2 and v1 <= v2) or (x2 < x1 and v2 <= v1):
    return "NO"