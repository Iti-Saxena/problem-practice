class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        
        for i in range(len(nums)):
            # If current index is beyond max_reach, we can't proceed
            if i > max_reach:
                return False
            
            # Update max_reach with the furthest we can jump from current index
            max_reach = max(max_reach, i + nums[i])
            
            # If we can reach the last index, return True
            if max_reach >= len(nums) - 1:
                return True
        
        return False


if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.canJump([2,3,1,1,4]) == True
    print("Test 1 passed: [2,3,1,1,4] -> True")
    
    # Test case 2
    assert solution.canJump([3,2,1,0,4]) == False
    print("Test 2 passed: [3,2,1,0,4] -> False")
    
    # Test case 3
    assert solution.canJump([0]) == True
    print("Test 3 passed: [0] -> True")
    
    # Test case 4
    assert solution.canJump([1]) == True
    print("Test 4 passed: [1] -> True")
    
    # Test case 5
    assert solution.canJump([2,0,0]) == True
    print("Test 5 passed: [2,0,0] -> True")
    
    # Test case 6
    assert solution.canJump([0,2,3]) == False
    print("Test 6 passed: [0,2,3] -> False")
    
    # Test case 7
    assert solution.canJump([1,1,1,1]) == True
    print("Test 7 passed: [1,1,1,1] -> True")
    
    print("\nAll tests passed!")   