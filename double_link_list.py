'''
This program is an attempt to teach doubly linked list
A double linked list is similiar to a linked list, instead it has an extra previous prointer. It points to the previous node of the current node.
for example :
    1->2->3->4->5
    here for node with value 2 , previous node is the node with value 1,next node is the one with value 3.
'''

#This class is used to define the node properties needed for doubly_linked_list
class node(object):
    def __init__(self,val):
        self.data=val
        self.next=None
        self.prev=None

#class definition of the doubly_linked_list
class double_link(object):
    #The constructor defines the head node of the linked list
    def __init__(self):
        self.head=node(None)
        
    #The insert method, used to insert a value in the link_list
    def insert(self,val):
        x=node(val)
        k=self.head
        if k.next==None:
            k.next=x
            x.prev=k
        else:
            while k.next!=None:
                k=k.next
            k.next=x
            x.prev=k
            
    #This method performs link traversal and is used to print the node values of the doubly_linked_list
    def show(self,head):
        k=head
        if k.next==None:
            print 'Empty list'
        else:
            k=k.next
            while k.next!=None:
                print k.data,
                print '->',
                k=k.next
            print k.data
            
    #This method is used to delete a node from the linked list
    def delete(self,data):
        k=self.head
        if k.next==None:
            print 'empty list'
        else:
            print 'performing data deletion from doubly linked list'
            k=k.next
            while k.next.data!=data:
                k=k.next
            k.next=k.next.next
            k.next.prev=k
            
    #This method is used to search for a particular node in the linked list        
    def search(self,data):
        k=self.head
        self.is_found=0
        if k.next==None:
            print 'empty list'
        else:
            k=k.next
            while k.next!=None:
                if k.data==data:
                    print 'The searched value '+ str(data)+ ' found !'
                    self.is_found=1
                    break
                else:
                    k=k.next
                    continue
        if self.is_found==0:
           print 'Sorry, ' +str(data)+ ' does not exist'
            
            

dl=double_link()
a=[1,2,3,4,5,6,7,8]
for i in a:
    dl.insert(i)
dl.show(dl.head)
dl.search(15)
dl.delete(6)
dl.show(dl.head)
