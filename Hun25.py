class Node:
  def __init__(self,data):
    self.value=data
    self.right=None
    self.left=None

def insert(root,data):
  if root is None:
    root=Node(data)
  elif root.value > data:
    if root.left is None:
      root.left=Node(data)
    else:
      insert(root.left,data)
  elif root.value < data:
    if root.right is None:
      root.right=Node(data)
    else:
      insert(root.right,data)

def LCA(root,L_val,R_val):
  if root is None:
    return None
  elif L_val > root.value and R_val > root.value:
    return(LCA(root.right,L_val,R_val))
  elif L_val < root.value and R_val < root.value:
    return (LCA(root.left,L_val,R_val))
  else:
    return root.value

n=int(input())
val=list(map(eval,input().split()))
b,rs=map(eval,input().split())
R=Node(val[0])
for i in range(1,n):
  insert(R,val[i])
print(LCA(R,b,rs))
