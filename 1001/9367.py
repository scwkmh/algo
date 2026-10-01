T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    C = list(map(int, input().split()))

    cnt = 1  # 현재 증가 구간 길이
    long = 1  # 지금까지 최대 길이
    for i in range(N - 1):
        if C[i] < C[i + 1]:
            cnt += 1
        else:
            cnt = 1
        if cnt > long:
            long = cnt

    print(f"#{tc} {long}")