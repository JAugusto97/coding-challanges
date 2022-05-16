"""
Given an integer array nums and an integer k,
return the kth largest element in the array.

Note that it is the kth largest element in the sorted order,
not the kth distinct element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104

Solution:
* Using a min heap, iterate through the list and store the first K elements
* after the Kth element, start checking if the element is bigger than the top of the heap (smallest value)
* if its bigger, than swap it and restore the heap property
* if its not, continue.

Time Complexity: O(NlogN)
Space Complexity: O(K)
"""
from typing import List
from data_structures import MinHeap


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = MinHeap()
        for v in nums:  # O(l)
            if len(h) < k:
                h.insert(v)
            else:
                vmin = h.get_min()
                if v > vmin:
                    h.arr[0] = v
                    h.bubble_down()  # O(logl)

        return h.extract_min()
