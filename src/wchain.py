import sys

def max_chain_length(words):
    if not words:
        return 0
    word_set = set(words)
    min_len = min(len(w) for w in words)
    max_len = max(len(w) for w in words)
    buckets = [[] for _ in range(max_len + 1)]
    for w in word_set:
        buckets[len(w)].append(w)
    dp = {}
    best = 1
    for length in range(min_len, max_len + 1):
        for w in buckets[length]:
            cur = 1
            for i in range(len(w)):
                smaller = w[:i] + w[i+1:]
                if smaller in word_set:
                    cur = max(cur, dp[smaller] + 1)
            dp[w] = cur
            if cur > best:
                best = cur
    return best

def main():
    with open('wchain.in', 'r') as f:
        data = f.read().split()
    if not data:
        return
    n = int(data[0])
    words = data[1:1+n]
    result = max_chain_length(words)
    with open('wchain.out', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()