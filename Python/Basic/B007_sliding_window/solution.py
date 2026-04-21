arr = [4, 2, 1, 7, 8, 1, 2, 8]
k = 3

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum += arr[i]
    window_sum -= arr[i - k]
    
    max_sum = max(max_sum, window_sum)

print(max_sum)