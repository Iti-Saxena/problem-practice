class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1 = m - 1
        index2 = n - 1
        merged_index = m + n - 1
        
        # Merge arrays from the end
        while index1 >= 0 and index2 >= 0:
            if nums1[index1] > nums2[index2]:
                nums1[merged_index] = nums1[index1]
                index1 -= 1
            else:
                nums1[merged_index] = nums2[index2]
                index2 -= 1
            merged_index -= 1
        
        # If there are remaining elements in nums2, copy them to nums1
        while index2 >= 0:
            nums1[merged_index] = nums2[index2]
            index2 -= 1
            merged_index -= 1

        # # If there are remaining elements in nums1, copy them to nums1
        # while index1 >= 0:
        #     nums1[merged_index] = nums1[index1]
        #     index1 -= 1
        #     merged_index -= 1
        
        return nums1

test = Solution()
print(test.merge([1,2,3,0,0,0], 3, [2,5,6], 3))  # Expected output: [1,2,2,3,5,6]