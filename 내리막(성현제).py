T = int(input())    # 입력값을 T로 받기

for tc in range(1, T+1):    # 테스트 케이스를 1부터 T번 반복
    N = int(input())        # 입력값을 N으로 받기
    nA = list(map(int, input().split()))    # 한숫자 씩 띄어서 들어오는 수를 nA 리스트 자료형으로 받기
    answer = 0              # 변수 선언
    if N == 1:              # 자연수 N이 1개라면
        answer = 1          # 비교할 숫자가 없으므로, 감소조건 만족하는 1 출력
    else:
        for i in range(N-1):    # 자연수 N이 1이 아닌 경우이기에 범위를 N-1로 두어도 만족
            if nA[i] > nA[i+1]:     # 인덱스 i+1의 요소가 i보다 작다면 감소조건 만족, 1출력
                answer = 1
            elif nA[i] <= nA[i+1]:      # 인덱스 i+1의 요소가 i보다 크거나 같다면 감소조건 불만족, 0 출력
                answer = 0
                break                   # 한번만 규칙을 불만족하면 0 출력
    print(f"#{tc} {answer}")            # 테스트케이스와 답을 함꼐 출력
