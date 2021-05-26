import sys
input=sys.stdin.readline
import itertools 
import copy

class Soccer:
    def read(self):
        self.n=int(input())
        self.info=[]
        for _ in range(self.n):
            a=input().split()
            a=list(map(int,a))
            self.info.append(a)
        
    def solve(self):
        Min=float("inf")
        tm=self.n//2    #team member 
        u=[i for i in range(1,self.n)]
        s1=itertools.combinations(u,tm-1)
        s1=list(map(list,s1))
        for pairs in s1: # ex. i=0, pairs=[1,2] -> [0,1,2] 가 team 
            s_a=0
            s_b=0 
            pairs.append(0)
            info=copy.deepcopy(self.info)
            s2=itertools.combinations(pairs,2)
            s2=list(map(list,s2))
            c=[]
            for p in s2: # ex. [0,1] [0,2] [1,2]
                s_a+=self.info[p[0]][p[1]]
                s_a+=self.info[p[1]][p[0]]
                if p[0] not in c:
                    info[p[0]]=[0]*self.n
                if p[1] not in c:
                    info[p[1]]=[0]*self.n
                for i in range(self.n):
                    if p[0] not in c:
                        info[i][p[0]]=0
                    if p[1] not in c:
                        info[i][p[1]]=0
                c.append(p[0])
                c.append(p[1])
            for left in info:
                s_b+=sum(left)
            t=abs(s_a-s_b)
            if t<Min:
                Min=t 
      
            
        print(Min)           
         
s=Soccer()
s.read()
s.solve()       