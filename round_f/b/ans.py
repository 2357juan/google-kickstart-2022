import sys
sys.stdin = open("input.txt") # for debugging

from collections import defaultdict

def solve():
    N,Q = map(int,input().split())
    G = defaultdict(list)
    for _ in range(N-1):
        i,j = map(int,input().split())
        G[i].append(j)
        G[j].append(i)
    for _ in range(Q):
        input()
    seen = set()
    queue = [1]
    level = []
    ans = len(queue)
    while len(queue) != 0:
        node = queue.pop()
        seen.add(node)
        for child in G[node]:
            if child not in seen:
                level.append(child)
        if len(queue) == 0:
            if Q - ans >= len(level):
                ans += len(level)
                queue = level
                level = []
            else:
                break
    print(ans)
    return

if __name__ == "__main__":
    for i in range(1, int(input()) + 1):
        print(f"Case #{i}: ",end="")
        solve()