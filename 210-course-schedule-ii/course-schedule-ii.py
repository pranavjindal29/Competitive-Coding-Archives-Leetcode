from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> list:
        # Initialize graph and in-degree count
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        # Build the graph and in-degree array
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        
        # Find all nodes with zero in-degree
        zero_in_degree = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        # Perform topological sort
        order = []
        while zero_in_degree:
            course = zero_in_degree.popleft()
            order.append(course)
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    zero_in_degree.append(neighbor)
        
        # Check if all courses are in the order
        return order if len(order) == numCourses else []


        
        