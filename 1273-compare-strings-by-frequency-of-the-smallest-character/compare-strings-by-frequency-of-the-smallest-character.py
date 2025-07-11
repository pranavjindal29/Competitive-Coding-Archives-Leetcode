class Solution:
	def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
		def f(s):
			t = sorted(list(s))[0]
			return s.count(t)
		query = [f(x) for x in queries]
		word = [f(x) for x in words]
		m = []
		for x in query:
			count = 0
			for y in word:
				if y>x:
					count+=1
			m.append(count)
		return m