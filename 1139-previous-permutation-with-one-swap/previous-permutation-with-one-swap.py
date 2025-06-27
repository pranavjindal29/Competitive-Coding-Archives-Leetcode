class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        length = len(arr)
        for left in range(length - 2, -1, -1):
            if arr[left] > arr[left + 1]:
                right = left + 1
                swap_idx = right
                while right < length and arr[right] < arr[left]:
                    if arr[right] != arr[swap_idx]:
                        swap_idx = right
                    right += 1
                arr[left], arr[swap_idx] = arr[swap_idx], arr[left]
                break
        return arr