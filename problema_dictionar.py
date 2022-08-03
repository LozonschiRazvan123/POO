n=int(input())
dictt={}
for i in range(n):
    val=input().split()
    dictt[val[0]]=val[1]
while True:
    try:
        x=input()
        if x in dictt:
            print(x+'='+dictt[x])
        else:
            print('Not found')
    except EOFError:
        pass

# def isLengthEvenOrOdd(head):
#     nr=0
#     while head:
#         nr+=1
#         head=head.next
#     if nr%2==0:
#         print("Even")
#     else:
#         print("Odd")
#
# class Node:
#     def __init__(self,data,next=None):
#         self.data=data
#         self.next=next
# class LinkedList:
#     def __init__(self):
#         self.head=None
#     def append_list(self,data):
#         if not self.head:
#             self.head=Node(data)
#             return
#         curent=self.head
#         while curent.next:
#             curent=curent.next
#         curent.next=Node(data)
# def create(arr,n):
#     lis=LinkedList()
#     for i in range(n):
#         lis.append_list(arr[i])
#     return lis.head
# if __name__=='__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         arr = list(map(int, input().strip().split()))
#         head = create(arr, n)
#         isLengthEvenOrOdd(head)