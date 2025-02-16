class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        element_count = Counter(nums)
        
        majority_elements = []
        threshold = len(nums) // 3
        
        for element, count in element_count.items():
            if count > threshold:
                majority_elements.append(element)
        
        return majority_elements