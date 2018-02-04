#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def left_preOrder_recursive(tree,i):
    
    if i==-1:
      return
    
    left_preOrder_recursive(tree,tree[i][1])
    left.append(tree[i][0])
    left_preOrder_recursive(tree,tree[i][2])
def right_preOrder_recursive(tree,i):
    
    if i==-1:
      return
    
    right_preOrder_recursive(tree,tree[i][1])
    right.append(tree[i][0])
    right_preOrder_recursive(tree,tree[i][2])

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
    if tree==[]:
        return True
    
    if type(tree)==int:
        return True
    else:
    
        global left,right

        i = 0
        left = []
        right = []
        root_key = tree[i][0]
        left_node = tree[i][1]
        right_node = tree[i][2]

        left_preOrder_recursive(tree,left_node)
        right_preOrder_recursive(tree,right_node)
        left.append(root_key)
        left.extend(right)
        #print(left)
        for i in range(len(left)-1):
            if left[i]>left[i+1]:
                return False
            if left[i]==left[i+1] and i%2==0:
                return False
        return True
    

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []

  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
'''tree = [[4,1,2],[2,3,4],[6,5,6],[1,-1,-1],[3,-1,-1],[5,-1,-1],[7,-1,-1]]
tree1 = [[2,1,2],[1,-1,-1],[3,-1,-1]]
tree2 = [[1,1,2],[2,-1,-1],[3,-1,-1]]
tree3 = [[2,1,2],[1,-1,-1],[2,-1,-1]]
tree4 = [[2,1,2],[2,-1,-1],[3,-1,-1]]
tree5 = 0
tree6 = [[2147483647 ,-1,-1]]
tree7 = [[1,-1,1],[2,-1,2],[3,-1,3],[4,-1,4],[5,-1,-1]]
tree8 = [[4,1,2],[2,3,4],[6,5,6],[1,-1,-1],[3,-1,-1],[5,-1,-1],[7,-1,-1]]
if __name__ == "__main__":  # this means that the script was an argument for the interperet
    if IsBinarySearchTree(tree8):
        print("CORRECT")
    else:
        print("INCORRECT")'''
