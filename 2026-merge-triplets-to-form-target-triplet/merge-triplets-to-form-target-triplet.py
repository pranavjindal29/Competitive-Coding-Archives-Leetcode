class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [False] * len(target)

        for triplet in triplets:
            x, y, z = triplet
            if x == target[0] and y <= target[1] and z <= target[2]:
                res[0] = True
            if y == target[1] and x <= target[0] and z <= target[2]:
                res[1] = True
            if z == target[2] and x <= target[0] and y <= target[1]:
                res[2] = True
        
        return res[0] and res[1] and res[2]