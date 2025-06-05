from collections import defaultdict

def dfs(graph, start, end=None):
    """
    Perform Depth-First Search (DFS) on a graph. sdfretretre
    
    Args:
        graph: Dictionary representing the graph as adjacency list
        start: Starting vertex for DFS
        end: (Optional) Target vertex to find distance to
        
    Returns:
        If end is None: list of vertices in DFS order
        If end is specified: distance from start to end or None if no path exists
        
    Raises:
        ValueError: If start or end vertices are not in the graph
    """

    if start not in graph:
        raise ValueError(f"Start vertex {start} not found in graph")
    if end is not None and end not in graph:
        raise ValueError(f"End vertex {end} not found in graph")
    
    visited = set()
    stack = [(start, 0)]  
    path = []
    distance = None
    
    while stack:
        vertex, dist = stack.pop()
        if vertex == end:
            distance = dist
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
  
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append((neighbor, dist + 1))
    
    if end is not None:
        return distance
    return path

def build_graph(edges):
    # sfsdf
    """
    Build an adjacency list representation of a graph from edge list.
    
    Args:
        edges: List of tuples representing undirected edges
        
    Returns:
        Dictionardfdfasdsady where keys dfare vertices and values are lists of adjacent vertices
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

if __name__ == "__main__":
    edges = [(4, 2), (1, 3), (2, 4)]
    graph = build_graph(edges)
    print(dfs(graph, 22, 4))  
