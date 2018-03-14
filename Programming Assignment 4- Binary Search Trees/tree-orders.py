# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def inOrder_recursive(self,node):
    if node==-1:
      return
    self.inOrder_recursive(self.left[node])
    self.result.append(self.key[node])
    self.inOrder_recursive(self.right[node])

  def preOrder_recursive(self,node):
    if node==-1:
      return
    self.result.append(self.key[node])
    self.preOrder_recursive(self.left[node])
    self.preOrder_recursive(self.right[node])

  def postOrder_recursive(self,node):
    if node==-1:
      return
    self.postOrder_recursive(self.left[node])
    self.postOrder_recursive(self.right[node])
    self.result.append(self.key[node])

  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.inOrder_recursive(0)
    return self.result

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.preOrder_recursive(0)         
    return self.result

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.postOrder_recursive(0)          
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
