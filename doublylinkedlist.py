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



    def insert_at_begining(self,data):
        itr=self.head
        if itr == None:
            self.head=Node(data,None,None)
            return

        new=Node(data,None,itr)
        itr.prev=new
        self.head=new


if __name__ == '__main__':
    ll=doublyll()

    ll.insert_at_begining(1)
    ll.insert_at_begining(2)
    ll.insert_at_begining(3)
    ll.insert_at_begining(4)
    ll.printll()

