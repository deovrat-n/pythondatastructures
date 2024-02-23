class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

class doublyll:
    def __init__(self):
        self.head=None
    
    def printll(self):
        itr=self.head
        if itr==None:
            print('list is empty')
            return
        
        li=[]
        while itr:
            li.append(itr.data)
            itr=itr.next

        k='-->'.join(str(i) for i in li)
        print(k)
    
    def getLen(self):
        itr=self.head
        count=0
        if itr ==None:            
            return count
        
        while itr:
            itr=itr.next
            count+=1
        
        return count



    def insert_at_begining(self,data):
        itr=self.head
        if itr == None:
            self.head=Node(data,None,None)
            return

        new=Node(data,None,itr)
        itr.prev=new
        self.head=new
    
    def insert_at_end(self,data):
        itr=self.head
        if itr==None:
            self.head=Node(data,None,None)
        
        while itr.next:
            itr=itr.next
        
        new=Node(data,itr,None)
        itr.next=new
    
    def insert_at_index(self,data,index):
        if index<0 or index>=self.getLen():
            raise Exception("INvalid Syntax")
        
        if index==0:
            self.insert_at_begining(data)
            return
        
        itr=self.head
        count=0
        while count<index:
            itr=itr.next
            count+=1
        
        nw=Node(data,itr.prev,itr)
        itr.prev.next=nw
        itr.prev=nw
    
    def remove_at(self,index):
        if index<0 or index>=self.getLen():
            raise Exception("Invalid Syntax")
        itr=self.head
        if index==0:
            self.head=itr.next
            itr.next=None
            self.head.prev=None
            return    


        count=0
        while count<index:
            itr=itr.next
            count+=1      

        
        
        if index == self.getLen()-1:
            itr.prev.next=itr.next
            return
        
        itr.next.prev=itr.prev
    
        
            

            


if __name__ == '__main__':
    ll=doublyll()

    ll.insert_at_begining(1)
    ll.insert_at_begining(2)
    ll.insert_at_begining(3)
    ll.insert_at_begining(4)
    
    ll.printll()
    ll.insert_at_end(5)
    ll.insert_at_end(6)
    ll.printll()
    ll.insert_at_index(80,0)
    ll.printll()
    ll.remove_at(6)
    ll.printll()
    ll.insert_at_index(50,5)
    ll.printll()

