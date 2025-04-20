import heapq
import time

cities = {
    "A": (0, 0),
    "B": (2, 1),
    "C": (4, 2),
    "D": (5, 5),
    "E": (1, 4)
}

roads = {
    "A": ["B", "E"],
    "B": ["A", "C"],
    "C": ["B", "D"],
    "D": ["C"],
    "E": ["A", "D"]
}

def manhattan_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + manhattan_distance(start, goal), 0, start, []))  # f, g, current, path
    visited = set()
    nodes_explored = 0
    
    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        
        if current in visited:
            continue
        
        visited.add(current)
        path = path + [current]
        nodes_explored += 1
        
        if current == goal:
            return path, nodes_explored
        
        for neighbor in roads[current]:
            if neighbor not in visited:
                g_new = g + 1
                f_new = g_new + manhattan_distance(neighbor, goal)
                heapq.heappush(open_list, (f_new, g_new, neighbor, path))
    
    return None, nodes_explored


def gbfs(start, goal):
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start, goal), start, []))  # f, current, path
    visited = set()
    nodes_explored = 0
    
    while open_list:
        f, current, path = heapq.heappop(open_list)
        
        if current in visited:
            continue
        
        visited.add(current)
        path = path + [current]
        nodes_explored += 1
        
        if current == goal:
            return path, nodes_explored
        
        for neighbor in roads[current]:
            if neighbor not in visited:
                heapq.heappush(open_list, (manhattan_distance(neighbor, goal), neighbor, path))
    
    return None, nodes_explored

def run_comparison(start, goal):
    # A* 
    start_time = time.time()
    a_star_path, a_star_nodes = a_star(start, goal)
    a_star_time = (time.time() - start_time) * 1000  # waktu dalam ms
    
    # GBFS
    start_time = time.time()
    gbfs_path, gbfs_nodes = gbfs(start, goal)
    gbfs_time = (time.time() - start_time) * 1000  # waktu dalam ms
    
    print("A*:")
    print(f"Path: {a_star_path}")
    print(f"Nodes explored: {a_star_nodes}")
    print(f"Time (ms): {a_star_time:.4f}")
    
    print("\nGBFS:")
    print(f"Path: {gbfs_path}")
    print(f"Nodes explored: {gbfs_nodes}")
    print(f"Time (ms): {gbfs_time:.4f}")

run_comparison("A", "D")
