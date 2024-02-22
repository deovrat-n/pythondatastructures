class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        


class LinkedList:
    def __init__(self):
        self.head=None
        
    
    def insert_at_begining(self,data):
        new=Node(data,self.head)
        self.head=new
    
    def insert_values(self,li):
        self.head=None
        for data in li:
            self.insert_at_end(data)
        return
    
    def remove_at(self,index):
        
        if index <0 or index >= self.getLen():
            raise Exception("Invalid Synatx")
        
        if index==0:
            itr=self.head
            self.head=itr.next
            itr.next=None
            return
        else:
            itr=self.head
            count=0
            
            while count < index-1:
                itr=itr.next
                count+=1
            
            itr.next=itr.next.next
            return
        
        
    def insert_at_end(self,data):
        itr = self.head
        if itr==None:
            self.head=Node(data,None)
            return
            
        while itr.next:
            itr=itr.next
        new=Node(data,None)
        itr.next=new
    
    def getLen(self):
        itr=self.head
        count=0
        if itr == None:
            return count
        
        while itr:
            count+=1
            itr=itr.next
        return count
    
    def insert_at(self,index,data):
        if index <0 or index >= self.getLen():
            raise Exception("Invalid Synatx")
            
        if index==0:
            self.insert_at_begining(data)
        else:
            itr=self.head
            count=0
            
            while count < index-1:
                itr=itr.next
                count+=1
            
            new=Node(data,itr.next)
            itr.next=new
                
        
    def insert_after(self,data_after,data):
        itr=self.head
        
        while itr:
            if itr.data==data_after:
                new=Node(data,itr.next)
                itr.next=new
            itr=itr.next
        
    def remove_by_value(self,data):
        
        itr=self.head
        if itr.data==data:
            self.remove_at(0)
            return
        
        fast=itr.next
        
        while fast:
            if fast.data==data:
                itr.next=fast.next
                fast.next=None
            itr=itr.next
            fast=fast.next
        
            
    def printll(self):
        itr=self.head
        list=[]
        while itr:
            list.append(str(itr.data))
            itr=itr.next
        s='-->'.join(i for i in list)
        print(s)
    
if __name__ == '__main__':

    ll=LinkedList()
    
    ll.insert_at_begining(1)
    ll.insert_at_begining(2)
    ll.insert_at_begining(3)
    ll.printll()
    ll.insert_at_end(5)
    ll.printll()
    ll.insert_at(2,10)
    ll.printll()
    ll.insert_at(0,80)
    ll.printll()
    ll.insert_at(4,85)
    ll.printll()
    ll.remove_at(1)
    ll.printll()
    ll.remove_at(0)
    ll.printll()
    ll.insert_after(85,56)
    ll.printll()
    ll.remove_by_value(85)
    ll.printll()


            