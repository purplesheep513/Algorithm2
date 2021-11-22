import sys
import heapq
V, E = map(int, sys.stdin.readline().rstrip().split())
start = sys.stdin.readline().rstrip()
INF = 10e9
graph = [[] for _ in range(V+1)]
DISTANCE = [INF for _ in range(V+1)]
for _ in range(E):
    node1, node2, distance = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(graph[node1], (distance, node2))

def dijkstra(start):
    
    return