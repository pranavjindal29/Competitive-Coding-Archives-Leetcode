class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        n = len(img1)

        # convert to bits
        bit1 = []
        bit2 = []
        for i in range(n):
            b1 = int("0b" + "".join(map(str, img1[i])), 2)
            b2 = int("0b" + "".join(map(str, img2[i])), 2)

            bit1.append(b1)
            bit2.append(b2)
        
        # bfs on operations
        queue = deque([(bit1, (0, 0))])
        seen = set((0,0))
        max_overlaps = 0

        while queue:
            bit, op = queue.popleft()
            if all([True if b == 0 else False for b in bit]):
                continue

            overlaps = 0
            for i in range(n):
                overlaps+=(bit[i]&bit2[i]).bit_count()
            max_overlaps = max(max_overlaps, overlaps)

            
            # add translations
            if  (op[0]+1, op[1]) not in seen:
                h_shifted_p = [b//2 for b in bit]
                queue.append((h_shifted_p, (op[0]+1, op[1])))
                seen.add((op[0]+1, op[1]))
            if  (op[0]-1, op[1]) not in seen:
                h_shifted_n = [(2*b & ~(1<<(n+1))) for b in bit]
                seen.add((op[0]-1, op[1]))
                queue.append((h_shifted_n, (op[0]-1, op[1])))
            if (op[0], op[1]+1) not in seen:
                v_shifted_p = [0] + bit[:-1]
                seen.add((op[0], op[1]+1))
                queue.append((v_shifted_p, (op[0], op[1]+1)))
            if (op[0], op[1]-1) not in seen:
                v_shifted_n = bit[1:] + [0]
                queue.append((v_shifted_n, (op[0], op[1]-1)))
                seen.add((op[0], op[1]-1))



        return max_overlaps

        