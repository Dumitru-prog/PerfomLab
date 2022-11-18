f = open('file3.txt')
nums = f.read().split()
for i in range(len(nums)):
    nums[i] = int(nums[i])
nums.sort()
median = nums[len(nums) // 2]
print(sum(abs(num - median) for num in nums))