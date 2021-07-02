A = int(input())
B = int(input())
C = int(input())

if max([A, B, C]) == A:
    print(1)
elif min([A, B, C]) == A:
    print(3)
else:
    print(2)
if max([A, B, C]) == B:
    print(1)
elif min([A, B, C]) == B:
    print(3)
else:
    print(2)
if max([A, B, C]) == C:
    print(1)
elif min([A, B, C]) == C:
    print(3)
else:
    print(2)