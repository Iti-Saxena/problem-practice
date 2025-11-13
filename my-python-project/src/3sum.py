class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        # n = len(nums)
        # for i in range(n):
        #     target = -nums[i]
        #     seen = set()
        #     for j in range(i + 1, n):
        #         need = target - nums[j]
        #         if need in seen:
        #             # sort the triplet locally to avoid duplicate permutations
        #             trip = tuple(sorted((nums[i], nums[j], need)))
        #             res.add(trip)
        #         seen.add(nums[j])
        # return [list(t) for t in res]

        while len(nums) >=3:
            nums.sort()
            first = nums[0]
            target = -first
            left, right = 1, len(nums) - 1
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    res.add((first, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
            # Remove all instances of 'first' to avoid duplicates
            nums = [num for num in nums if num != first]