def lone_sum(a, b, c):
    if a == b and a == c and b == c:
        return 0
    elif a == c:
        return b
    elif b == c:
        return a
    elif a == b:
        return c
    else:
        return a+b+c


result = lone_sum(1, 1, 1)
print(result)
