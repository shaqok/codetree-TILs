N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

'''
학생 수 배열: scores
M번 순회하며 해당하는 학생의 배열을 +1
K를 만족한다면 바로 루프를 멈추고 출력
루프가 끝날 때까지 없다면 -1

'''
scores = [0] * (N + 1)
has_reached = False
result = -1

for student_id in student:
    scores[student_id] += 1
    if scores[student_id] == K:
        result = student_id
        break

print(result)
