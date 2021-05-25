import sys
input=sys.stdin.readline
import itertools 

class Soccer:
    def read(self):
        self.n=int(input())
        self.info=[]
        for _ in range(self.n):
            a=input().split()
            a=list(map(int,a))
            self.info.append(a)
        self.players=[i for i in range(self.n)]
        self.score={}
        
    def solve(self):
        ch=[]
        Min=float("inf")
        t_a=list(itertools.combinations(self.players,self.n//2))
        t_a=list(map(set,t_a))
    
        for items in t_a:
            a=list(items)
            b=set(self.players)-items
            t_a.remove(b)
            b=list(b)
            s_a=0
            s_b=0
            for i in range(self.n//2-1):
                for j in range(i,self.n//2):
                    if a[i]+a[j] in self.score:
                        s_a+=self.score[a[i]+a[j]]
                    if a[i]+a[j] not in self.score:
                        s_a+=self.info[a[i]][a[j]]
                        s_a+=self.info[a[j]][a[i]]
                        self.score[a[i]+a[j]]=s_a
                    if b[i]+b[j] in self.score:
                        s_b+=self.score[b[i]+b[j]]
                    if b[i]+b[j] not in self.score:
                        s_b+=self.info[b[i]][b[j]]
                        s_b+=self.info[b[j]][b[i]]
                        self.score[b[i]+b[j]]=s_b
            if abs(s_a-s_b)<Min:
                Min=abs(s_a-s_b)
               
        print(Min)           
         
s=Soccer()
s.read()
s.solve()       