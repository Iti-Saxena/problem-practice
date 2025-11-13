class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dic = {}
        for each in nums:
            dic[each] = dic.get(each, 0) + 1

        majority_key = max(dic, key=dic.get)
        return majority_key
obj = Solution()
print(obj.majorityElement([3,2,3]))  # Expected output is 3