import heapq


def solution(scoville, K):
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)
    count = 0
    while(len(heap) != 1 and heap[0] < K):
        minFirst = heapq.heappop(heap)
        minNext = heapq.heappop(heap)
        result = minFirst+2*minNext
        heapq.heappush(heap, result)
        count += 1
    if heap[0] < K:
        return -1
    return count


scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))
