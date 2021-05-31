import sys
input=sys.stdin.readline

class RGB:
    def read(self):
        self.hn=int(input())
        self.info=[]
        for i in range(self.hn):
            [interior]=list(map(int,input().split()))
            self.info.append(interior)
            interior=sorted(interior)
            self.c.append([interior[0]-interior[1],i,interior[0]])
    
    def solve(self):
        summ=0
        route=[]
        self.c=sorted(key=lambda x:x[0],ascending=True)
        for house in self.c:
            price=self.info[house[1]][house[2]]
            color=self.info[house[1]].index(price)
            if len(route)==0:
                route.append(color)
                summ+=price
            else:
                if color ==route[-1]:
                    color=self.info[house[1]].index(price+house[0])
                    summ+=price+house[0]
                    route.append(color)
                else:
                    summ+=price
                    route.append(color)
                
        
           

rgb=RGB()
rgb.read()
rgb.solve()                  
                