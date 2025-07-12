class Solution:
    def nthUglyNumber(self, n, a_, b_, c_):

        # mod = 10**9 + 7

        l = min(a_, b_, c_)
        r = n * min(a_, b_, c_)

        lcm_ab = math.lcm(a_, b_)
        lcm_ac = math.lcm(a_, c_)
        lcm_bc = math.lcm(b_, c_)
        lcm_abc = math.lcm(a_, b_, c_)

        while l < r:

            m = l + r >> 1

            a = m // a_
            b = m // b_
            c = m // c_
            ab = m // lcm_ab
            ac = m // lcm_ac
            bc = m // lcm_bc
            abc = m // lcm_abc

            if n <= (a + b + c - ab - ac - bc + abc):  
                r = m
            else:
                l = m + 1

        return l 