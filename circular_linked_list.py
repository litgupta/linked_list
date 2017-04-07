'''
This code is to demonstrate the circular linked list.
Circular linked list is same like doubly linked list, instead it has its last node pointing to the header node .
Circular linked list is used in many real world applications, some being :
-Time sharing in operating systems
-In a multiplayer_game to keep count of whose turn is next.
-It can also be used in a repeat mode music playlist , where the last song will point to the first song. 
'''

#A simple class defining the node properties of the circular linked list node, notice that we have made a circular
#linked list from a doubly linked list
class node(object):
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
#A class definition of the circular linked list
class circular_list(object):
    #Constructor for the circular linked list, which defines the header node
    def __init__(self):
        self.head=node(None)

    def insert(self,val):
        x=node(val)
        x.next=self.head
        k=self.head
        if k.next==None:
            k.next=x
            x.prev=k
        else:
            while k.next!=self.head:
                k=k.next
            k.next=x
            
    def show(self,head):
        k=head
        if k.next==None:
            print 'empty list'
        else:
            k=k.next
            while k.next!=self.head:
                print k.data,
                print '->',
                k=k.next
            print k.data
            
    def delete(self,data):
        k=self.head
        if k.next==None:
            print 'empty list'
        else :
            if self.search(data):
                print 'Deleting ' +str(data) 
                while k.next.data!=data:
                    k=k.next
                k.next=k.next.next
                k.next.prev=k
            else:
                print 'sorry the value does not exist in the list'

    def search(self,data):
        self.is_found=0
        k=self.head
        if k.next==None:
            self.is_found=0
        else:
            k=k.next
            while k.next!=self.head:
                if k.data==data:
                    is_found=1
                    break
                else:
                    k=k.next
                    continue
            return self.is_found


#main function
cl=circular_list()
a=[1,2,3,4,5,6,7,8]
for i in a:
    cl.insert(i)
cl.show(cl.head)
cl.delete(5)

