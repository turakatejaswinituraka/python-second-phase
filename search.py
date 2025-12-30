class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
def search(root,element):
    if root==None:
        return False
    if root.data==element:
        return True
    elif element< root.data:
        return search(root.left,element)
    else:
         return search(root.right,element)
root=Node(10)
root.left=Node(20)
root.left.left=Node(40)
root.right=Node(30)
root.right.left=Node(50)
print(search(root,10))
print(search(root,50))
