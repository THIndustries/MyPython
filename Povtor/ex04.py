nums: list[int] = list(map(int, input().split()))
count:int = 0
for i in range(len(nums) - 1):
    if nums[i+1] > nums[i]:
        count += 1
print(count)