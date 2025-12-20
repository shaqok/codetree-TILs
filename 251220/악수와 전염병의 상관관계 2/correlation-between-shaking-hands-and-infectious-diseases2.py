N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

'''
N - 개발자 수 -> infected = ['0'] * (N + 1)
K - 각 개발자의 악수의 수 (K번의 악수 동안만 전염, 그 이후엔 전염 X)
P - 처음 전염된 개발자 index
T - 악수 기록 for t in range(T):                                                                                                                                                                                       

handshakes = [(t초에, x가, y와 악수)]
handshakes 배열을 시간순으로 오름차순으로 정렬

infected_info 배열 필요 개발자 index 순으로 각 악수를 체크:
    [(2, '1')]
infected_info[P][1] = '1' 로 초기세팅

handshakes를 순회하며 infected_info에서 개발자별 기록 수정
! 감염된다면 K만큼 전염 가능
! 악수를 한 양쪽의 K를 차감해야 함
! 이미 전염된 개발자끼리의 악수도 K 차감    
'''
infected_info = [(0, '0')] * (N + 1)
infected_info[P] = (K, '1')

handshakes = sorted(handshakes, key=lambda x: x[0])
for handshake in handshakes:
    t, x, y = handshake

    k_x, i_x = infected_info[x]
    k_y, i_y = infected_info[y]
    prev_i_x, prev_i_y = i_x, i_y

    # 이미 둘 다 k가 0인 경우 생략 가능
    if k_x == k_y == 0: pass
    elif (i_x == '1' and k_x > 0) or (i_y == '1' and k_y > 0):
        i_x = i_y = '1'

    # 둘 다 k 차감
    if prev_i_x == '0' and i_x == '1':
        k_x = 2
    elif prev_i_x == '1' and k_x > 0:
        k_x -= 1

    if prev_i_y == '0' and i_y == '1':
        k_y = 2
    elif prev_i_y == '1' and k_y > 0:
        k_y -= 1

    infected_info[x] = (k_x, i_x)
    infected_info[y] = (k_y, i_y)


result = [info[1] for info in infected_info[1:]]
print(''.join(result))