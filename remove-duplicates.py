from typing import List
def removeDuplicates(self, nums: List[int]) -> int:
    i=len(nums)-1
    c = len(nums)
    while i>1:
        if nums[i]==nums[i-2]:
            nums.append(nums.pop(i))
            c-=1
        i-=1
    return c
