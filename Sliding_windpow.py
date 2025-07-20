from collections import deque

def sliding_window_max(nums, k):
    d = deque()
    result = []
    
    for i,n in enumerate(nums): #i = index, n = number
        while d and nums[d[-1]] <= n: #현재 숫자보다 작거나 같은 인덱스는 덱에서 제거
            d.pop()
        d.append(i) #현재 인덱스를 덱에 추가
        
        if d[0] == i - k: #맨 앞에 있는 인덱스가 윈도우 범위를 벗어났다면 제거
            d.popleft()
        if i >= k - 1: #윈도우가 완성 되었으면, d[0]에 해당하는 숫자 결과에 추가
            result.append(nums[d[0]])
    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_max(nums, k))