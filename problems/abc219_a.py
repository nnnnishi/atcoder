from typing import NewType


N = int(input())
if N < 40:
    a = 40 - N
elif 40 <= N < 70:
    a = 70 - N
elif 70 <= N < 90:
    a = 90 - N
else:
    print("expert")
    exit()
print(a)
