n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
arr = [0] * 200


for segment in segments:
    start, end = segment[0] + 100, segment[1] + 100
    for i in range(start, end):
        arr[i] += 1

print(max(arr))
        
