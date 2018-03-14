#Uses python3
import sys
import math
class Edge:
    def __init__(self,a,b,c):
        self.left = a
        self.right = b
        self.weight = c
def weight(x,y,i,j):
    length = ((x[i]-x[j])**2+(y[i]-y[j])**2)**(0.5)
    return length

def get_parent(node):
    global parent
    if node!=parent[node]:
        get_parent(parent[node])
    return parent[node]

def merge(left,right):
    global rank
    global parent
    global parent_list
    l_parent = get_parent(left)
    r_parent = get_parent(right)
    if l_parent!=r_parent:
        if rank[l_parent]>rank[r_parent]:
            parent[r_parent] = l_parent
            parent_list.remove(r_parent)
        elif rank[l_parent]==rank[r_parent]:
            rank[l_parent]+=1
            parent[r_parent] = l_parent
            parent_list.remove(r_parent)
        else:
            parent[l_parent] = r_parent
            parent_list.remove(l_parent)
    else:
        pass
def clustering(x, y, k):
    #write your code here
    global rank
    global parent
    global parent_list
    n = len(x)
    edges = []
    rank = [1] * n
    parent = list(range(0, n))
    parent_list = set(range(0, n))
    for i in range(n):
        for j in range(i+1,n):
            edges.append(Edge(i,j,weight(x,y,i,j)))
    edges = sorted(edges, key=lambda edge: edge.weight)
    
    for i in range(len(edges)):
        if get_parent(edges[i].left)!=get_parent(edges[i].right) and len(parent_list)==k:
            return edges[i].weight
            
        merge(edges[i].left,edges[i].right)
        

    return -1






if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    '''x = [3, 1, 4, 9, 9, 8, 3, 4]
    y = [1, 2, 6, 8, 9, 9, 11, 12]
    k = 4
    x = [7, 4, 5, 1, 2, 5, 3, 7, 2, 4, 6, 2]
    y = [6, 3, 1, 7, 7, 7, 3, 8, 8, 4, 7, 6]
    k = 3'''
    print("{0:.9f}".format(clustering(x, y, k)))
