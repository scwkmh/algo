# 왜 도움을 받아야 했는가?
# 반복문 선언시 범위 지정이 서툴렀음. 단순히 익숙하지 않았다는 말로는 치부할 수 없음
# N-M+1을 회문, 파리 등 다양한 문제에서 써먹을 수 있었는데 쓰면서 정작 어떤 원리인지 모름
# 원리는 가장 기본적으로 N-M을 마지막 인덱스로 둔다는 거임.
# "길이(크기)가 고정된 연속 덩어리를 전체 위에서 한 칸씩 밀면서 다 확인하는 문제'
# 해당 유형의 문제
# 1차원 구간합 - 4835 구간합
# 2차원 부분 격자 - 2001 파리 퇴치
# 문자열 패턴 - 4864 문자열 비교, 1213 String
# 회문 - 4861 회문 (N×N에서 길이 M 회문 찾아 출력), 1215 회문1 (길이 고정, 개수 세기)
#        1216 회문2 (가장 긴 회문, 가변 길이)
# 연속 칸 검사 (변형) - 11315 오목 판정, 1979 어디에 단어가 들어갈 수 있을까
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
    # 주의할 점: 줄 끝 공백
    #
    # 각 줄 끝에 공백이 하나 남아(c 뒤). SWEA는 보통 줄 끝 공백을 무시해서 통과되는데,
    # 엄격한 채점기면 틀릴 수 있어. 깔끔하게 하려면 한 행을 리스트에 모았다가
    # join으로 찍으면 돼.

    # for i in range(N - M + 1):
    #     row = []
    #     for j in range(N - M + 1):
    #         energy = 0
    #         for k in range(M):
    #             for l in range(M):
    #                 energy += n[i + k][j + l] + m[k][l]
    #         row.append(energy)
    #     print(' '.join(map(str, row)))


