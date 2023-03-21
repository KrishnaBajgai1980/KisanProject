def gapFun(a):
    if a > 0:
        x = a + gapFun(a-1)
        print(x)
    else:
        x = 0
        return x
gapFun(5)