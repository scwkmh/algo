T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    n = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    total = []
    for i in range(N):
        for j in range(3):
            x = n[i][0] * 0.35 + n[i][1] * 0.45 + n[i][2] * 0.2
            total.append(x)
            st = sum(total) // N
            if total[K-


    print(f"#{tc} {ans}")