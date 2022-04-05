# 수학적 접근으로 최적화
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split())) 

ans = 0
key = 0

# 첫 값 저장
temp = min(nums)
gap = 0
for i in range(n - 1):
    if key == 0:
        gap = max(nums) - min(nums)
        ans += gap
        nums.remove(min(nums))
        key = 1
        
    else:
        gap = max(nums) - min(nums)
        ans += gap
        nums.remove(max(nums))
        key = 0
if gap < nums[0] - temp:
    ans -= gap
    ans += nums[0] - temp
        
print(ans)