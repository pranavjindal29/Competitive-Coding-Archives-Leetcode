class Solution:
    def goodTriplets(self, nums1, nums2):
        n = len(nums1)
        pos = [0] * n
        for i in range(n):
            pos[nums2[i]] = i
        nums1 = [pos[x] for x in nums1]

        bit1 = [0] * (n + 2)
        bit2 = [0] * (n + 2)

        def update(bit, i, val):
            i += 1
            while i <= n:
                bit[i] += val
                i += i & -i

        def query(bit, i):
            i += 1
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        ans = 0
        for i in reversed(range(n)):
            x = nums1[i]
            val = query(bit1, n - 1) - query(bit1, x)
            trip = query(bit2, n - 1) - query(bit2, x)
            ans += trip
            update(bit2, x, val)
            update(bit1, x, 1)

        return ans