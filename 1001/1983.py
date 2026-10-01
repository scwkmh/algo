T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(N)]
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    total = []
    for i in range(N):
        t = scores[i][0] * 0.35 + scores[i][1] * 0.45 + scores[i][2] * 0.2
        total.append(t)

    F = total[K - 1]
    total.sort(reverse=True)
    g = N // 10
    total = [total[i:i + g] for i in range(0, N, g)]

    ans = ''
    for j in range(10):
        if F in total[j]:
            ans = grade[j]
            break

    print(f"#{tc} {ans}")