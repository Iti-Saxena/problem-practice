class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
    
        # k are the numbers of elements in the array nums which are not equal to val.
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
            
        return k
    
test = Solution()
print(test.removeElement([3,2,2,3], 3))  # Expected output: 2