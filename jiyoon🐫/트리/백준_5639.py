import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readlines

class BST:
    def read(self):
        self.tree=input()
        self.tree=[int(str.rstrip()) for str in self.tree]
        self.answer=[]
        
    
    def solve(self,a):
        top=a[0]
        left=[item for item in a if item<top]
        right=[item for item in a if item>top]
        #left 가 있다면
        if len(left)>0:
            self.solve(left)
        #right 이 있다면
        if len(right)>0:
            self.solve(right)
    
        self.answer.append(top)
            
    def Answer(self):
        self.solve(self.tree)
        for node in self.answer:
            print(node,end='\n')
    
    
bst=BST()
bst.read()
bst.Answer()