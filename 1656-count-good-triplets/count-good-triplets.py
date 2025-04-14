class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        good_triplets = 0
        length = len(arr)

        for i in range(length):  # i is the first index
            for j in range(i + 1, length):  # j must be after i
                if abs(arr[i] - arr[j]) <= a:  # first condition check
                    for k in range(j + 1, length):  # k must be after j
                        # Check all three conditions
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            good_triplets += 1
                            # \U0001f94b Rock Lee: "Another success from persistence!" \U0001f973
        
        return good_triplets