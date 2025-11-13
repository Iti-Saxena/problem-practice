class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # for i in range(len(numbers)):
        #     sec_number = target - numbers[i]
        #     if sec_number in numbers[i+1:]:
        #         j = numbers.index(sec_number, i + 1)
        #         return [i+1, j+1]
        # return []   # time complexity O(n^2) due to 'in' operator inside loop

        seen = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in seen:
                return [seen[complement] + 1, i + 1]  # +1 for 1-based indexing
            seen[num] = i
        return []  # time complexity O(n) due to single pass and O(1) lookups in dictionary
    
        # TODO two pointer approach can be implemented as well since the array is sorted

