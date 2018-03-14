# python3
import sys

n, m = map(int, sys.stdin.readline().split()) #n个列表 m个指令
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)
act = {}

def getParent(table):
    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]

def merge(destination, source):
    global ans
    Destination, Source = getParent(destination), getParent(source)
    lineRoot = 0

    if Destination == Source:
        return False

    if rank[Destination] > rank[Source]:
        parent[Source] = Destination
        lines[Destination] += lines[Source]
        lineRoot = lines[Destination]
        lines[Source] = 0

    elif rank[Destination] == rank[Source]:
        parent[Source] = Destination
        lines[Destination] += lines[Source]
        lineRoot = lines[Destination]
        lines[Source] = 0
        rank[Destination] += 1

    else:
        parent[Destination] = Source
        lines[Source] += lines[Destination]
        lineRoot = lines[Source]
        lines[Destination] = 0

    if lineRoot > ans:
        ans = lineRoot


    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)
