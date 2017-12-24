import sys

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            node=Node(data)
            node.next = self.head
            self.head = node

    def append(self,data):
        if self.head is None:
            print("\nYou need to enter something first to append brother!")
        else:
            curr=self.head
            while(curr.next != None):
                curr = curr.next
            node = Node(data)
            curr.next = node
    
    def display(self):
        if (self.head == None):
            print("\nList is Empty\n")
        else:
            curr=self.head  
            while(curr.next != None):
                print(curr.data)
                curr=curr.next
            print(curr.data)


if __name__=='__main__':
##    L = LinkedList()
##    L.head=Node(1)
##    L.first=Node(2)
##    L.second=Node(3)
##    L.head.next = L.first
##    L.first.next = L.second
##    L.display()

    #inserting values from the head of the list (prepend)
    n1 = int(input("\nEnter the number of values you wish prepend: "))
    i=0
    L=LinkedList() # REMEMBER BRO, THIS NEEDS TO BE DECLARED HERE. IF DECLARED INSIDE THE LOOP IT ONLY ENDS UP PRINTING THE LAST VALUE
    while(i<n1):
        val = int(input("\nEnter data: "))
        L.prepend(val)
        i=i+1
    L.display()

    #inserting values from the tail of the list (appending)
    n2 = int(input("\nEnter the number of values you wish append: "))
    i=0
    while(i<n2):
        val = int(input("\nEnter data: "))
        L.append(val)
        i=i+1
    L.display()
