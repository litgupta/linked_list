class node(object):
    def __init__(self,val):
        self.data=val
        self.next=None
        
class link_list(object):
    def __init__(self):
        self.head=node(None)

    def insert(self,val):
        k=self.head
        x=node(val)
        if k.next==None:
            k.next=x
        else:
            while k.next!=None:
                k=k.next
            k.next=x

    def show(self):
        k=self.head
        if k==None:
            print 'Empty list'
        else:
            k=k.next
            while k.next!=None:
                print k.data,
                print '->',
                k=k.next
            print k.data
    def delete(self,z):
        k=self.head
        if k.next==None:
            print 'empty list'
        else:
            k=k.next
            while k.next.data!=z:
                k=k.next
            k.next=k.next.next

            

l=link_list()
a=[1,2,3,4,5,6,7,8,9]
for i in a:
    l.insert(i)
l.show()
l.delete(5)
l.show()
