def find_missing(m, n):
    len_m = len(m)
    len_n = len(n)
    if len_m == len_n:
        return 0
    else:
        for i in n:
            if i not in m:
                return i