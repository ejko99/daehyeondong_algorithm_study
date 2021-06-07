#python 3 
import sys
class DisjointSet:
    def read(self):
        self.item_num,self.operation_num=map(int,input().split())
        self.union_question=[]
        self.root=[i for i in range(self.item_num+1)]
        self.rank=[0]*len(self.root)
        for _ in range(self.operation_num):
            self.union_question.append(list(map(int,sys.stdin.readline().split())))
    
    def find(self,a):
        if self.root[a]==a:
            return a
        else:
            return self.find(self.root[a])
    
    def union_by_rank(self,a,b):
        A=self.find(a)
        B=self.find(b)
        if A==B:
            return
        elif self.rank[A]>self.rank[B]:
            self.root[B]=A
        else:
            self.root[A]=B
            if self.rank[A]==self.rank[B]:
                self.rank[B]+=1
                
    def solve(self):
        for item in self.union_question:
            if item[0]==0:
                self.union_by_rank(item[1],item[2])
            else:
                if self.find(item[1])==self.find(item[2]):
                    print("YES",end='\n')
                else:
                    print("NO",end='\n')

disjoint=DisjointSet()
disjoint.read()
disjoint.solve()