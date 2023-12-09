from typing import Optional


class Node:
    def __init__(self,value):
        self.value = value
        self.next: Optional[Node] = None


#constructor
class LinkedList:
    def __init__(self,value):
       new_node = Node(value) # create a new node calling class Node
       self.head = new_node #make it point to 1st node created, same as tail
       self.tail = new_node
       self.length = 1 # keep track of count

    def appendList(self,value):
        new_node = Node(value)
        if self.tail is None:
            new_node = (self.head,self.tail)
            #self.head = new_node
            #self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

    def append(self,value):
        new_node = Node(value)
        if self.head is None: #if there is no new node
            self.head = new_node #point head and tail to the remaining one 
            self.tail = new_node
        else:
            self.tail.next = new_node #else the tail.next is assigned to new_node
            self.tail = new_node # i guess its the same. tail  assigned to new_node
        self.length +=1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next



my_linked_list = LinkedList(1)
#print(my_linked_list.head.value)
#my_linked_list.appendList(3)
#my_linked_list.print_list()
my_linked_list.append(2)
my_linked_list.print_list()




