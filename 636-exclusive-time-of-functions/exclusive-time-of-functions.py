class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack, res = [], [0] * n
        for log in logs:
            id, func, curr_time = log.split(":")
            id, curr_time = int(id), int(curr_time)
            if func == "start":
                stack.append((id, curr_time))
            elif func == "end" and id == stack[-1][0]:
                pop_id, insert_time = stack.pop()
                time_taken = curr_time - insert_time + 1
                res[pop_id] += time_taken
                if stack:
                    res[stack[-1][0]] -= time_taken 
        return res
        