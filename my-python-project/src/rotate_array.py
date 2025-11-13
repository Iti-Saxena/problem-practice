class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for iter in range(0,k):
            last_element=nums[-1]
            for i in range(len(nums)-1,0,-1):
                nums[i]=nums[i-1]
            nums[0]=last_element


        # solution using slicing
        # k = k % len(nums)  # In case k is greater than the length of the array
        # nums[:] = nums[-k:] + nums[:-k]  
        

obj=Solution()
nums=[1,2,3,4,5,6,7]
