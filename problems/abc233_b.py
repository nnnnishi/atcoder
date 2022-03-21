L, R = list(map(int, input().split()))
S = list(input().rstrip())
print("".join(S[: L - 1] + S[L - 1 : R][::-1] + S[R:]))
