class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_begin(self,data):
        node = Node(data)
        if (self.head == None):
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        else:
            curr=self.head
            while (curr.next != None):
                curr=curr.next
            curr.next = node
            node.prev = curr

    def display(self):
        if (self.head is None):
            print("\nThe list is empty\n")
        else:
            current = self.head
            while(current.next != None):
                print(current.data)
                current = current.next
            print(current.data)

    def insert(self,data,pos):
        if(self.head == None):
            print("\nThe list is empty\n")
        else:
            i=0
            temp = self.head
            curr = self.head
            while(i<pos-1):
                  curr = curr.next
                  i = i+1
            node = Node(data)
            node.next = curr.next
            curr.next.prev = node
            node.prev = curr
            curr.next = node

              
    def del_begin(self):
        if(self.head == None):
            print("\nList is empty\n")
        else:
            curr = self.head
            curr = curr.next
            self.head = curr
            self.head.prev = None

    def del_end(self):
        if self.head is None:
            print("\nList is empty\n")
        else:
            curr = self.head
            while(curr.next.next != None): 
                curr = curr.next
            curr.next = None 

    def del_pos(self,pos):
        if self.head is None:
            print("\nList is empty\n")
        else:
            curr = self.head
            i=1
            while(i<=pos):
                curr = curr.next
                i=i+1
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
                

if __name__=='__main__':       
    print("\n---------- Implementation a double linked list ----------\n")
    print("\n<1> To Enter a value at the beginning of the list")
    print("\n<2> To Enter a value at the end of the list")
    print("\n<3> To Print the list")
    print("\n<4> To Insert a value at a particular position in the list")
    print("\n<5> To Delete a value from the beginning")
    print("\n<6> To Delete a value from the end")
    print("\n<7> To Delete a value from a particular postion")
    print("\n<0> To EXIT\n")
    l= LinkedList() # This always need to be defined ONLY ONCE
    while(1):
        choice = int(input("\nEnter choice: "))

        if (choice == 1):
            val=int(input("\nEnter the data: "))
            l.add_begin(val)

        if (choice == 2):
            val=int(input("\nEnter the data: "))
            l.append(val)

        if choice is 3:
            l.display()

        if choice is 4:
            val = int(input("\nEnter the value you wish to insert: "))
            pos = int(input("\nEnter the position where you wish to insert: "))
            if pos is 0:
                l.add_begin(val)
            else:
                l.insert(val,pos)            
            l.display()

        if choice is 5:
            l.del_begin()

        if choice is 6:
            l.del_end()

        if choice is 7:
            pos = int(input("\nEnter the position which you wish to delete: "))
            if pos is 0:
                l.del_begin()
            else:
                l.del_pos(pos)

        if choice is 0:
            exit()
