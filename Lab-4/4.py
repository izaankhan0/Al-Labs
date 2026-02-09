graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

def dls(graph, start, goal, limit):
    visited = []
    def dfs(node, depth):
        if depth > limit:
            return None
        
        visited.append(node)
        
        if node == goal:
            print(f"Goal found: {visited}")
            return visited
        
        for i in graph.get(node, []):
            if i not in visited:
                path = dfs(i, depth + 1)
                if path:
                    return path
        visited.pop()
        return None
    result = dfs(start, 0)
    
    if not result:
        print("not found")
    return result

start_node = 'A'
goal_node = 'H'

print("DLS")
dls(graph, start_node, goal_node, 3)