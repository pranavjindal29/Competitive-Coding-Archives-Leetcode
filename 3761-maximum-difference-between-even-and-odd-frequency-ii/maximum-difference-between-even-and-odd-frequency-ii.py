import numpy as np

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        arr = np.frombuffer(s.encode('ascii'), dtype=np.uint8) - ord('0')
        pre = np.empty((5, n), dtype=np.int64)
        for x in range(5):
            is_x = (arr == x).astype(np.int64)
            pre[x] = np.cumsum(is_x)
        closest_right = np.full((5, n), n, dtype=np.int64)
        for x in range(5):
            indices = np.flatnonzero(arr == x)
            if indices.size:
                pos = np.searchsorted(indices, np.arange(n))
                valid = pos < indices.size
                closest_right[x, valid] = indices[pos[valid]]
        
        best = -10**9
        for odd in range(5):
            for even in range(5):
                if odd == even:
                    continue
                odd_pre = pre[odd]
                even_pre = pre[even]
                
                odd_parity = (odd_pre % 2).astype(np.int64)
                even_parity = (even_pre % 2).astype(np.int64)
                
                suf = np.full((2, 2, n), -10**9, dtype=np.int64)
                
                valid_mask = (odd_pre > 0) & (even_pre > 0)
                diff = odd_pre - even_pre
                idx = np.where(valid_mask)[0]
                
                suf[odd_parity[idx], even_parity[idx], idx] = diff[idx]
                
                
                for p in (0, 1):
                    for q in (0, 1):
                        suf[p, q] = np.maximum.accumulate(suf[p, q][::-1])[::-1]
                
                m = n - k + 1
                start_idx = np.arange(m, dtype=np.int64)

                odd_below = np.where(start_idx == 0, 0, odd_pre[start_idx - 1])
                even_below = np.where(start_idx == 0, 0, even_pre[start_idx - 1])
                
                good_odd_parity = (odd_below + 1) % 2
                good_even_parity = even_below % 2
               
                q1 = start_idx + k - 1
                q2 = closest_right[odd, start_idx]
                q3 = closest_right[even, start_idx]
                query = np.maximum.reduce([q1, q2, q3])
                
                valid_q = query < n
                candidate = -10**9 * np.ones(m, dtype=np.int64)
                
                for p in (0, 1):
                    for q in (0, 1):
                        mask = (good_odd_parity == p) & (good_even_parity == q) & valid_q
                        if np.any(mask):
                            candidate[mask] = np.maximum(candidate[mask],
                                                         suf[p, q][query[mask]] - odd_below[mask] + even_below[mask])
                best = max(best, candidate.max())
        return int(best)