class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        d = {}
        menus = set()

        for _, tn, fi in orders:
            if tn not in d:
                d[tn] = {}

            if fi not in d[tn]:
                d[tn][fi] = 1
            else:
                d[tn][fi] += 1

            menus.add(fi)

        menus = sorted(list(menus))
        ans = [["Table"] + menus]

        for key in sorted([int(x) for x in list(d.keys())]):
            k = str(key)
            r = [k]
            
            for m in menus:
                if m not in d[k]:
                    r.append("0")
                else:
                    r.append(str(d[k][m]))

            ans.append(r)

        return ans