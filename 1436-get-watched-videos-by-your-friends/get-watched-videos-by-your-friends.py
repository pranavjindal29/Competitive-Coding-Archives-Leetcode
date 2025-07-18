class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        watched_dict = defaultdict(int)
        q = deque()
        q.append(id)
        visited = set()
        visited.add(id)
        dist = 1
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                for nei in friends[curr]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            if dist == level:
                break
            else:
                dist+=1
        for user in q:
            for vid in watchedVideos[user]:
                watched_dict[vid]+=1
        
        watched_dict = {k: v for k, v in sorted(watched_dict.items(), key=lambda item: [item[1], item[0]])}
        
        return list(watched_dict.keys())