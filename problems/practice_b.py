from string import ascii_uppercase


def compare(a, b):
    print("? " + a, b)
    return input()


def sort5(l):
    a, b, c, d, e = l
    if compare(a, b) == ">":
        a, b = b, a
    if compare(c, d) == ">":
        c, d = d, c
    if compare(a, c) == ">":
        a, b, c, d = c, d, a, b
    if compare(c, e) == "<":
        if compare(d, e) == ">":
            d, e = e, d
        if compare(b, d) == "<":
            if compare(b, c) == "<":
                l = [a, b, c, d, e]
            else:
                l = [a, c, b, d, e]
        else:
            if compare(b, e) == "<":
                l = [a, c, d, b, e]
            else:
                l = [a, c, d, e, b]
    else:
        if compare(a, e) == "<":
            if compare(b, c) == "<":
                if compare(b, e) == "<":
                    l = [a, b, e, c, d]
                else:
                    l = [a, e, b, c, d]
            else:
                if compare(b, d) == "<":
                    l = [a, e, c, b, d]
                else:
                    l = [a, e, c, d, b]
        else:
            if compare(b, c) == "<":
                l = [e, a, b, c, d]
            else:
                if compare(b, d) == "<":
                    l = [e, a, c, b, d]
                else:
                    l = [e, a, c, d, b]
    return l


def merge_sort(l):
    if len(l) <= 1:
        return l

    mid = len(l) // 2
    left = l[:mid]
    right = l[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    l_i, r_i = 0, 0

    while l_i < len(left) and r_i < len(right):

        print("? " + left[l_i], right[r_i])
        if input() == "<":
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1

    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])
    return merged


n, q = map(int, input().split())
ans = list(ascii_uppercase[:n])
ans = merge_sort(ans) if n != 5 else sort5(ans)

print("! " + "".join(ans), flush=True)
