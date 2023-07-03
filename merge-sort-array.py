from typing import List
from heapq import heappush, heappop

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:

    """Using Pointers

    Returns:
        _type_: _description_
    """
    num_1_pointer, num_2_pointer, write_index = m-1, n-1, m+n-1
    while num_2_pointer>=0:
        if num_1_pointer>=0 and nums1[num_1_pointer]>nums2[num_2_pointer]:
            nums1[write_index] = nums1[num_1_pointer]
            num_1_pointer-=1
        else:
            nums1[write_index] = nums2[num_2_pointer]
            num_2_pointer-=1
        write_index-=1
    # return nums1

    """
    Using Heap
    """
    # merge = []
    # for i in nums1[:m]:
    #     heappush(merge, i)
    # for j in nums2:
    #     heappush(merge, j)
    # for k in range(m+n):
    #     nums1[k] = heappop(merge)


nums1 = [2,0]
m = 1
nums2 = [1]
n = 1

print(merge(
    nums1=nums1,
    m=m,
    nums2=nums2,
    n=n
))