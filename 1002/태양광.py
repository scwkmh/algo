T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    n = [list(map(int, input().split())) for _ in range(N)]
    m = [list(map(int, input().split())) for _ in range(M)]
    # 출력 방식때문에 먼저 선언
    print(f'#{tc}')
    # 가로 및 세로 리스트의 마지막 인덱스는 N-M이다.
    for i in range(N-M+1):
        for j in range(N-M+1):
            # 에너지의 총합을 담을 변수 생성
            energy = 0
            # 태양광 판넬의 크기를 이중 반복문으로 표현
            for k in range(M):
                for l in range(M):
                    # n 배열 중 태양광 판넬과 겹치는 값을 더해주기
                    energy += n[i+k][j+l] + m[k][l]
            print(energy, end=' ')
        print()

    # 엄격한 방식
    # for i in range(N - M + 1):
    #     row = []
    #     for j in range(N - M + 1):
    #         energy = 0
    #         for k in range(M):
    #             for l in range(M):
    #                 energy += n[i + k][j + l] + m[k][l]
    #         row.append(energy)
    #     print(' '.join(map(str, row)))

