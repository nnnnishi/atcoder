# 拡張ユークリッドの互除法
# ax+by = gとなるx,yをみつける
# code: https://tjkendev.github.io/procon-library/python/math/gcd.html
# O(log max(a,b))

# 2つ以上の最小公約数
def extgcd(a, b):
    """
    return (g,x,y)
    """
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b) * x
        return d, x, y
    return a, 1, 0


print(extgcd(3, 9))