# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
     def levelOrder(self, root):
        solution=[]
        if root == None:
            return solution
        levelToProcess =[root]
        while len(levelToProcess)>0:
            numbersLevel =[]
            nextLevel = []
            for temp in levelToProcess:
                numbersLevel.append(temp.val)
                if temp.left != None:
                    nextLevel.append(temp.left)
                if temp.right != None:
                    nextLevel.append(temp.right)
            solution.append(numbersLevel)
            levelToProcess = nextLevel
        return solution