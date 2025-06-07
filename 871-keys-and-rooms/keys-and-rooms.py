class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited_rooms = set()
        stack = [0] # for rooms that we need to visit and we start from room [0]
        
        while stack: 
            room = stack.pop() 
            visited_rooms.add(room)
            for key in rooms[room]:
                if key not in visited_rooms:
                    stack.append(key)
        return len(visited_rooms) == len(rooms)            
            