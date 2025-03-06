class Solution:
	def __init__(self, nums: List[int]):
		self.arr = nums[:]

	def reset(self) -> List[int]:
		return self.arr

	def shuffle(self) -> List[int]:
		ans = self.arr[:]
		for i in range(len(ans)):
			swp_num = random.randrange(i, len(ans)) 
			ans[i], ans[swp_num] = ans[swp_num], ans[i]
		return ans