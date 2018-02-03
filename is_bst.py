#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def left_preOrder_recursive(tree,i):
    
    if i==-1:
      return
    left.append(tree[i][0])
    left_preOrder_recursive(tree,tree[i][1])
    left_preOrder_recursive(tree,tree[i][2])
def right_preOrder_recursive(tree,i):
    
    if i==-1:
      return
    right.append(tree[i][0])
    right_preOrder_recursive(tree,tree[i][1])
    right_preOrder_recursive(tree,tree[i][2])

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  global left,right
  
  for i in range(len(tree)):
    
    left = []
    right = []
    root_key = tree[i][0]
    left_node = tree[i][1]
    right_node = tree[i][2]

    left_preOrder_recursive(tree,left_node)
    right_preOrder_recursive(tree,right_node)

    
    if len(right)!=0 and root_key >= min(right):
      return False

    
    if len(left)!=0 and root_key <= max(left):
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
'''tree = [[1,1,2],[2,-1,-1],[3,-1,-1]]
if __name__ == "__main__":  # this means that the script was an argument for the interperet
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")'''
