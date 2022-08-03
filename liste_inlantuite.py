class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        if not self.head:
            self.head=Node(data)
            return
        curent=self.head
        while curent.next:
            curent=curent.next
        curent.next=Node(data)

    def insertAtBeginning(self, new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def remove(self,target):
        if self.head==target:
            self.head=self.head.next
            return
        curent=self.head
        previous=None
        while curent:
            if curent.data==target:
                previous.next=curent.next
            previous=curent
            curent=curent.next

    def reverse_list(self):
        curent=self.head
        previous=None
        while curent:
            next=curent.next
            curent.next=previous
            previous=curent
            curent=next
        self.head=previous


    def sortedLinkedList(self):
        previous =self.head
        while previous.next:
            curent=previous.next
            while curent.next:
                if previous.data>curent.data:
                    previous.data,curent.data=curent.data,previous.data
                curent=curent.next
            previous=previous.next


    def dublu(self):
        curent=self.head
        if curent.data%2==1:
            nod=Node(next)
            nod.data=curent.data*2
            nod.next=curent.next
            curent.next=nod
        while curent.next:
            if curent.data.next%2==1:
                nod=Node(next)
                nod.data = curent.data * 2
                nod.next = curent.next
                curent.next = nod
                curent=curent.next
            else:
                curent=curent.next



    def __str__(self):
        node=self.head
        while node.next is not None:
            print(node.data)
            node=node.next


a_list=LinkedList()
a_list.append(1)
a_list.append(2)
a_list.append(3)
a_list.append(5)
a_list.append(8)
a_list.append(10)
a_list.remove(3)
a_list.insertAtBeginning(21)
a_list.reverse_list()
a_list.sortedLinkedList()
a_list.dublu()
a_list.__str__()