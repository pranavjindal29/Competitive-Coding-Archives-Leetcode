class Solution:
	def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

		horizontalCuts = [0] + horizontalCuts + [h]
		verticalCuts = [0] + verticalCuts + [w]

		horizontalCuts.sort()
		verticalCuts.sort()

		horizontal_max = -1
		vertical_max = -1

		for index in range(1, len(horizontalCuts)):
			horizontal_max = max(horizontal_max, horizontalCuts[index]-horizontalCuts[index-1])

		for index in range(1, len(verticalCuts)):
			vertical_max = max(vertical_max, verticalCuts[index]-verticalCuts[index-1])

		return (horizontal_max * vertical_max) % ((10**9)+7)