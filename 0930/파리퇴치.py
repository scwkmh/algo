T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    nn = [list(map(int, input().split())) for _ in range(N)]
    x = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            s = 0
            # M x M 만큼의 정사각형 모양의 합을 구해야함. 지금은 M = 2라는 걸 확정지음
            for k in range(M):
                for l in range(M):
                    s += nn[i+k][j+l]
            x.append(s)

    print(f"#{tc} {max(x)}")
