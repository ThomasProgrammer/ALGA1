def is_bipartite(graph, n):
    color = [-1] * (n + 1)
    
    def bfs(start):
        queue = [start]
        color[start] = 0
        
        while queue:
            node = queue.pop(0)
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True
    
    for i in range(1, n + 1):
        if color[i] == -1:
            if not bfs(i):
                return False
    return True

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    scenarios = int(data[index])
    index += 1
    results = []
    
    for scenario in range(1, scenarios + 1):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        
        graph = [[] for _ in range(n + 1)]
        
        for _ in range(m):
            u = int(data[index])
            v = int(data[index + 1])
            index += 2
            graph[u].append(v)
            graph[v].append(u)
        
        if is_bipartite(graph, n):
            results.append(f"Scenario #{scenario}:\nNo suspicious bugs found!")
        else:
            results.append(f"Scenario #{scenario}:\nSuspicious bugs found!")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()