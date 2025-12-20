n = int(input())
arr = [int(input()) for _ in range(n)]

'''

'''

if n == 1:
    print(1)

max_freq = 0

prev_i = 0
for i in range(n):
    if i == 0 or arr[i] != arr[i-1]:
        freq = i - prev_i
        max_freq = max(max_freq, freq)
        prev_i = i

print(max_freq)
    