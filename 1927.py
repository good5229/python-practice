import heapq
import sys

n = int(sys.stdin.readline().strip())
heap = []
for i in range(n):
    cmd = int(sys.stdin.readline().strip())
    if cmd == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, cmd)


# 11279

n = int(sys.stdin.readline().strip())
heap = []
for i in range(n):
    cmd = int(sys.stdin.readline().strip())
    if cmd == 0:
        if heap:
            print(-1 * heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, (-cmd))