from typing import List
def removeElement(self, nums: List[int], val: int) -> int:

    counter = len(nums)
    for i in range(len(nums)-1, -1, -1):
        if nums[i]==val:
            counter-=1
            if i!=len(nums)-1:
                nums.append(nums.pop(i)) 
    return counter