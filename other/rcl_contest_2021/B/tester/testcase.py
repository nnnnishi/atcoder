import random

N = 40
MAX_E = 30


class TestCase:

    def __init__(self, seed=None, input=None):
        if seed is not None:
            self.N = N
            self.E = [[0] * N for _ in range(N)]
            random.seed(seed)
            prob = [0.0] + [1.0 / (i * i) for i in range(1, MAX_E + 1)]
            total_prob = sum(prob)
            for i in range(self.N):
                for j in range(self.N):
                    x = random.random() * total_prob
                    self.E[i][j] = MAX_E
                    for k in range(1, MAX_E + 1):
                        x -= prob[k]
                        if x <= 0:
                            self.E[i][j] = k
                            break
        else:
            itr = iter(input)
            self.N = int(next(itr))
            self.E = []
            for i in range(self.N):
                self.E.append(list(map(int, next(itr).split())))

    def __str__(self):
        ret = "%d\n" % (self.N, )
        return ret + "\n".join(" ".join(str(v) for v in row) for row in self.E)
