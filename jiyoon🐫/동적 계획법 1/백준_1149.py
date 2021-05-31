import sys
input=sys.stdin.readline

class RGB:
    def read(self):
        self.hn=int(input())
        self.info=[list(map(int,input().split())) for _ in range(self.hn)]
    
    def solve(self):
        info=self.info.copy()
        p1=min(info[0])
        summ=p1
        c1=info[0].index(p1)
        info[1][c1]=float("inf")
        r1=[p1]
        for i in range(1,self.hn):
            p1=min(info[i])
            c1=info[i].index(p1)
            if i<self.hn-1:
                info[i+1][c1]=float("inf")
            summ+=p1
            r1.append(p1)
            info2=self.info.copy()
            r=i
            summ2=0
            p2=min(info2[i])
            if p2==r1[-1]:
                continue
            summ2+=p2
            r2=[p2]
            r-=1
            print(r,end='\n')
            c2=info2[0].index(p2)
            info2[i-1][c2]=float("inf")
            while r>0:
                p2=min(info2[r])
                c2=info2[r].index(p2)
                info2[r-1][c2]=float("inf")
                summ2+=p2 
                r-=1
                r2.append(p2)
                print(r2)
            if summ>summ2:
                r1=r2
                summ=summ2 
        print(r1,end='r1\n')
        print(summ)     
rgb=RGB()
rgb.read()        
rgb.solve()           
                