from os import pread
from tempfile import tempdir
from typing import Optional


class Node:
    def __init__(self,value=None):
        self.value = value
        self.next: Optional[Node] = None
        #self.next : Node


#constructor
class LinkedList:
    def __init__(self,value):
       new_node = Node(value) # create a new node calling class Node
       self.head = new_node #make it point to 1st node created, same as tail
       self.tail = new_node
       self.length = 1 # keep track of count

    def pop(self,value):
        if self.head is None:
            return False
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.length -=1
        return True # kaya pla ang behaviour is it removes NOT the one i supplied as value
    

    def pop1(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head

        #while (temp.next):
        while temp.next is not None:
        #and temp.value != value:
            pre = temp 
            temp = temp.next 
        
        if temp is None:
            return None
        
        if pre is None:
            self.head = temp.next
        else:
            pre.next = temp.next

        #self.tail = pre
        #self.tail.next = None
        
        self.length -=1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value





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



my_linked_list = LinkedList(3)

my_linked_list.append(1)

my_linked_list.print_list()

#my_linked_list.pop(3)

#input("press enter to clear sceen")

#print('\033c', end='')
print(my_linked_list.pop1())
print(my_linked_list.pop1())
print(my_linked_list.pop1())
my_linked_list.print_list()




