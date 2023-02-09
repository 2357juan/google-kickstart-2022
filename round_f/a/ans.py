# import sys
# sys.stdin = open("input.txt") # for debugging

def solve():
    ans = 0
    N = int(input())
    F = []
    for _ in range(N):
        c,d,u = input().split()
        d,u = int(d),int(u)
        F.append((c,d,u))
    ada = sorted(F,key=lambda x:(x[0],x[2]))
    charles = sorted(F,key=lambda x:(x[1],x[2]))
    for (*_,u1),(*_,u2) in zip(ada,charles):
        if u1 == u2:
            ans += 1
    print(ans)

if __name__ == "__main__":
    for i in range(1, int(input()) + 1):
        print(f"Case #{i}: ",end="")
        solve()