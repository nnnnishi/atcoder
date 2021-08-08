from decimal import Decimal

A, B = [_ for _ in input().split()]
print(int(Decimal(A) * Decimal(B)))
