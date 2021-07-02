A, B, C = list(map(int, input().split()))
if A == B:
    print("=")
else:
    if C % 2 == 0:
        if abs(A) == abs(B):
            print("=")
        elif abs(A) > abs(B):
            print(">")
        else:
            print("<")
    else:
        if A < 0 and B < 0:
            if A < B:
                print("<")
            else:
                print(">")
        elif A >= 0 and B >= 0:
            if A < B:
                print("<")
            else:
                print(">")
        elif A >= 0 and B < 0:
            print(">")
        elif A < 0 and B >= 0:
            print("<")
