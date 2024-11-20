from collections import deque

def network_delay_time(times, n, k):
    # Initialize the graph with an adjacency list
    graph = {}
    for u, v, w in times:
        if u not in graph:
            graph[u] = []
        graph[u].append((v, w))

    # Initialize the distance list
    dist = [float('inf')] * (n + 1)
    dist[k] = 0

    # Initialize the heap
    heap = deque([(0, k)])

    # Loop through the heap
    while heap:
        time, node = heap.popleft()
        if node in graph:
            for neighbor, delay in graph[node]:
                if time + delay < dist[neighbor]:
                    dist[neighbor] = time + delay
                    heap.append((time + delay, neighbor))

    # Get the maximum delay
    max_delay = max(dist[1:])
    return max_delay if max_delay < float('inf') else -1

if __name__ == '__main__':
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    print(f'Input:\ntimes = {times}\nn = {n}\nk = {k}')
    print(network_delay_time(times, n, k))
    print()

    times = [[1, 2, 1]]
    n = 2
    k = 1
    print(f'Input:\ntimes = {times}\nn = {n}\nk = {k}')
    print(network_delay_time(times, n, k))
    print()

    times = [[1, 2, 1]]
    n = 2
    k = 2
    print(f'Input:\ntimes = {times}\nn = {n}\nk = {k}')
    print(network_delay_time(times, n, k))
    print()

