'''                                            DP ON TREES                                   '''

'''
Given a binary tree, find the diameter of the binary tree.
Diameter of binary tree is longest path between 2 leaf nodes
'''

class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

final_answer = -float('inf')
def find_diameter(root):
    solve(root)
    return final_answer
def solve(root):
    global final_answer
    if root==None:
        return 0
    
    l = solve(root.left)
    r = solve(root.right)

    # if node does not want to become diameter
    temp = max(l, r) + 1

    final_answer = max(final_answer, 1+l+r)

    return temp

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
# Function Call
print(find_diameter(root))