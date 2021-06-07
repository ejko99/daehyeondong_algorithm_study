# python3
import sys


class Findnumber:
    def read(self):
        self.task_num = int(input())
        self.exist_list=list(map(int, sys.stdin.readline().split()))
        self.item_num=int(input())
        self.search_list=list(map(int, sys.stdin.readline().split()))



    def binary(self):
        answer=[]
        self.exist_list=sorted(self.exist_list)
        done=0
        for item in self.search_list:
            low=0
            high=len(self.exist_list)-1
            while low<=high:
                mid=(low+high)//2
                done=0
                if item == self.exist_list[mid]:
                    answer.append(1)
                    done+=1
                    break
                elif item > self.exist_list[mid]:
                    low=mid+1
                elif item < self.exist_list[mid]:
                    high=mid-1
            if done!=1:
              answer.append(0)
        for item in answer:
            print(item,end='\n')













findnumber = Findnumber()
findnumber.read()
findnumber.binary()
