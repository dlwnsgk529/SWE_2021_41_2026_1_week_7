from typing import List

def twoSum(nums : List[int], target: int) -> List[int]:
    n = len(nums)
    
    for num1 in range(n):
        for num2 in range(num1 + 1, n):
            if nums[num1] + nums[num2] == target:
                return [num1, num2]

    return []


