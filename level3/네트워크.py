from collections import deque


def solution(n, computers):
    q = deque()
    count = 0
    visit = [False for _ in range(n)]

    while False in visit:
        x = visit.index(0)
        q.append(x)
        visit[x] = True

        while q:
            node = q.popleft()

            for i in range(n):
                if not visit[i] and computers[node][i] == 1:
                    q.append(i)
                    visit[i] = True
        count += 1
    return count

# 3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
# 3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1
