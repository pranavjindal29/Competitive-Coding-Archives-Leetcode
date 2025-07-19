class Solution:
    def printVertically(self, s):
        return [''.join(a).rstrip() for a in itertools.zip_longest(*s.split(), fillvalue=' ')]