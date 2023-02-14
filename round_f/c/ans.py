import os
import heapq
import sys
from collections import defaultdict,namedtuple

# sys.stdin = open("input.txt") # for interactive debugging otherwise comment out
# sys.stdin = open("test_data/test_set_3/ts3_input.txt") # for interactive debugging otherwise comment out
# sys.stdout = open("output.txt")

class Plant:

    def __init__(self,q,l,v,d):
        self.q = q
        self.l = l
        self.v = -v # heap is a minheap
        self.d = d

    def __lt__(self,p):
        if self.v < p.v:
            return True
        return False

# def solve1():
#     D,N,X = map(int,input().split())
#     plants = []
#     for _ in range(N):
#         q,l,v = map(int,input().split())
#         plants.append(Plant(q,l,v,D-l))
    
#     def rec(day,plants,N):
#         if day > N or len(plants) == 0:
#             return 0
#         ans = 0

#         for i in range(len(plants)):
#             if day <= plants[i].d:
#                 ans = max(ans,plants[i].v + rec(day+1,plants[:i] + plants[i+1:],N))
#             else:
#                 ans = max(ans,rec(day+1,plants[:i] + plants[i+1:],N))
#         return ans
#     print(rec(1,plants,N))


def solve3():
    D,N,X = map(int,input().split())
    plants = []
    for _ in range(N):
        q,l,v = map(int,input().split())
        plants.append(Plant(q,l,v,D-l))
    plants.append(Plant(0,0,0,0))
    plants.sort(key=lambda x:x.d,reverse=True)
    heap = []
    ans = 0
    for i,j in zip(plants,plants[1:]):
        heapq.heappush(heap,i)
        if i.d == j.d:
            continue
        seeds = X * (i.d-j.d)
        while len(heap) > 0 and seeds > 0:
            n = heap[0]
            q = min(seeds,n.q)
            ans += q * -n.v
            seeds -= q
            n.q -= q
            if n.q == 0:
                heapq.heappop(heap)
    print(ans)


if __name__ == "__main__":
    for i in range(1, int(input()) + 1):
        print(f"Case #{i}:",end=" ")
        solve3()