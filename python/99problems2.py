from bisect import bisect_left, bisect_right

class UF:
    def __init__(self, n, b):
        self.uf = [-1] * n
        self.b = b

    def find(self, node):
        while self.uf[node] != node:
            node = self.uf[node]
            self.uf[node] = self.uf[self.uf[node]]
        return node

    def union(self, n1, n2):
        r1, r2 = self.find(n1), self.find(n2)
        self.uf[r2 if self.b else r1] = r1 if self.b else r2

    def check(self, node):
        if not 0 <= node < len(self.uf):
            return -1
        elif self.uf[node] == -1:
            return node
        res = self.find(node) + (-1) ** self.b
        return res if 0 <= res < len(self.uf) else -1

    def add(self, node):
        if self.uf[node] != -1:
            return
        self.uf[node] = node
        if node and self.uf[node - 1] != -1:
            self.union(node - 1, node)
        if node + 1 < len(self.uf) and self.uf[node + 1] != -1:
            self.union(node, node + 1)

n, q = map(int, input().split())
lst = sorted(map(int, input().split()))
uf1, uf2 = UF(n, True), UF(n, False)

for _ in range(q):
    t, d = map(int, input().split())
    check = uf2.check(bisect_left(lst, d + 1)) if t == 1 else uf1.check(bisect_right(lst, d) - 1)
    print(-1 if check == -1 else lst[check])
    if check != -1:
        uf1.add(check)
        uf2.add(check)
