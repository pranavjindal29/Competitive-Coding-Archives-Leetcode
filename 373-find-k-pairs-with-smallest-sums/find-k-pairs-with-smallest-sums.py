from heapq import heappop, heappush
from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        # storing the length of nums1 to use it in a loop later
        list_length = len(nums1)
        # declaring a min-heap to keep track of the smallest sums
        min_heap = []
        # to store the pairs with smallest sums
        pairs = []

        # iterate over the length of nums1
        for i in range(min(k, list_length)):
            # computing sum of pairs of all elements of nums1 with first index
            # of nums2 and placing it in the min-heap
            heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        counter = 1

        # iterate over elements of min-heap and only go up to k
        while min_heap and counter <= k:
            # placing sum of the top element of min-heap
            # and its corresponding pairs in i and j
            sum_of_pairs, i, j = heappop(min_heap)

            # add pairs with the smallest sum in the new list
            pairs.append([nums1[i], nums2[j]])

            # increment the index for nums2, as we've
            # compared all possible pairs with the 1st index of nums2
            next_element = j + 1

            # if next element is available for nums2 then add it to the heap
            if len(nums2) > next_element:
                heappush(min_heap, (nums1[i] + nums2[next_element], i, next_element))

            counter += 1

        # return the pairs with the smallest sums
        return pairs