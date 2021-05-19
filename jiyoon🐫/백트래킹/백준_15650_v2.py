from collections import deque
import sys
input=sys.stdin.readline

class NM:
    def read(self):
       self.N,self.M=map(int,input().split())
       self.st=1
       d=1 #devision
       for i in range(self.N,self.N-self.M,-1):
           self.st*=i
       for i in range(1,self.M+1):
           d*=i
       self.st=self.st//d
       
    def BFS(self): #BFS
        use=[str(i) for i in range(1,self.N+1)]
        c=0
        ch_n=[] #checked number
        for i in range(1,self.N+1):
            search_queue=deque()
            search_queue+=[str(i)]
            root=str(i)
            while search_queue:
                person=search_queue.popleft()
                if len(person)-(self.M-1)==self.M:
                    c+=1
                    print(person) 
                    if c==self.st:
                        return     
                else:
                    root=person 
                    search_queue+=[root+' '+item for item in use if int(item) > int(root[-1]) and item not in ch_n]
        
                    
            ch_n.append(str(i))
nm=NM()
nm.read()
nm.BFS()