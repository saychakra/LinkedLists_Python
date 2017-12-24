class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class slist:
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
            while (curr.next):
                curr=curr.next
            curr.next=node

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
            i=1
            curr = self.head
            while(i<pos):
                curr = curr.next
                i=i+1
            temp = curr
            curr = curr.next
            node = Node(data)
            temp.next = node
            node.next = curr
            
               
    def del_begin(self):
        if(self.head == None):
            print("\nList is empty\n")
        else:
            curr = self.head
            curr = curr.next
            self.head = curr

    def del_end(self):
        if self.head is None:
            print("\nList is empty\n")
        else:
            curr = self.head
            while(curr.next.next != None): # I'll move to the second last node
                curr = curr.next
            curr.next = None #then simply put None in its next part with a smirk!

    def del_pos(self,pos):
        if self.head is None:
            print("\nList is empty\n")
        else:
            curr = self.head
            i=1
            while(i<pos-1):
                curr = curr.next
                i=i+1
            curr.next = curr.next.next

    def search_pos(self,val):
        if (self.head is None):
            print("\nThe list is empty\n");
        else:
            curr = self.head
            i=0
            flag = 0
            if(curr.data == val):
                print("\nValue found at position ",i)
            else:
                while(curr.next is not None):
                    curr = curr.next
                    i = i+1
                    if(curr.data == val):
                        print("\nValue found at position ", i)
                        flag = 1
                        break;
                if (flag == 0):
                    print("\nValue not found in the list\n")

    def no_of_node(self):
        if (self.head == None):
            return 0
        else:
            curr = self.head
            i=1
            while(curr.next != None):
                  curr = curr.next
                  i = i+1
        return i


if __name__=='__main__':       
    print("\n---------- Implementation a singly linked list ----------\n")
    print("\n<1> To Enter a value at the beginning of the list")
    print("\n<2> To Enter a value at the end of the list")
    print("\n<3> To Print the list")
    print("\n<4> To Insert a value at a particular position in the list")
    print("\n<5> To Delete a value from the beginning")
    print("\n<6> To Delete a value from the end")
    print("\n<7> To Delete a value from a particular postion")
    print("\n<8> To search for a particular value");
    print("\n<9> To count the number of nodes in the list")
    print("\n<10> To sort the existing list in ascending order")
    print("\n<0> To EXIT\n")
    l= slist() # This always need to be defined ONLY ONCE
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

        if choice is 8:
            val = int(input("\nEnter the value you wish to search for: "))
            l.search_pos(val)

        if choice is 9:
            count = l.no_of_node()
            print("\nThe number of nodes in the list is: ", count)

        if choice is 0:
            exit()
