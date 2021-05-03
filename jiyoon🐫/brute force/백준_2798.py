import sys
input=sys.stdin.readline

class BlackJack:
    def read(self):
        self.N,self.M=map(int,input().split())
        self.items=list(map(int,input().split()))
    
    def solve(self):
        a=sorted(self.items,reverse=True)
        small=a[-1]
        best=float("inf")
        for i in range(len(a)):
            c=self.M
            ad=a.copy()
            ad.remove(a[i])
            c=self.M-a[i]
            for item in ad:
                c2=c
                if item<=c2-small:
                    c2-=item
                    ad.remove(item)
                    if c2<self.M-a[i]:
                        for item in ad:
                            c3=c2
                            if item<=c3:
                               c3-=item
                               if c3 ==0:
                                  print(self.M)
                                  return 

                               elif c3<best:
                                  best=c3
                    
                    else: #첫번째 선택값이 너무 커서 세 개를 담지 못하는 경우
                        continue

      
        
        print(self.M-best)
            
            
        
        
        
        
black=BlackJack()
black.read()
black.solve()