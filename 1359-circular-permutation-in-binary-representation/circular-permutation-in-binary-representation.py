class Solution:
	def circularPermutation(self, n: int, start: int) -> List[int]:
		res=[]
		for i in range(2**n):
			res.append(i^(i>>1))
		stack=[]
		tem=[]
		for j in range(len(res)):
			if res[j]!=start:
				stack.append(res[j])
			else:
				tem=res[j:]
				break
		ans=tem+stack
		return ans