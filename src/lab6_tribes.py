import sys


class UnionFind:

    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            return x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return
        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        elif self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        else:
            self.parent[yr] = xr
            self.rank[xr] += 1


def count_pairs(pairs):
    uf = UnionFind()
    for a, b in pairs:
        uf.union(a, b)

    tribe_males = {}
    tribe_females = {}

    for person in uf.parent.keys():
        rep = uf.find(person)
        if person % 2 == 1:
            tribe_males[rep] = tribe_males.get(rep, 0) + 1
        else:
            tribe_females[rep] = tribe_females.get(rep, 0) + 1

    total_males = sum(tribe_males.values())
    total_females = sum(tribe_females.values())
    result = total_males * total_females

    for rep in tribe_males:
        males = tribe_males.get(rep, 0)
        females = tribe_females.get(rep, 0)
        result -= males * females

    return result


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    pairs = []
    idx = 1
    for _ in range(n):
        if idx + 1 >= len(data):
            break
        a = int(data[idx])
        b = int(data[idx + 1])
        pairs.append((a, b))
        idx += 2
    result = count_pairs(pairs)
    print(result)


if __name__ == "__main__":
    main()