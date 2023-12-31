from tempfile import tempdir
from typing import Optional


class Node:
    def __init__(self,value=None):
        self.value = value
        self.next: Optional[Node] = None
        self.prev = None


#constructor
class LinkedList:
    def __init__(self,value=None):
       new_node = Node(value) # create a new node calling class Node
       self.head = new_node #make it point to 1st node created, same as tail
       self.tail = new_node
       self.length = 1 # keep track of count


    def append(self,value): #sumpay sa last sa index
        new_node = Node(value)
        if self.head is None: #if there is no new node
            self.head = new_node #point head and tail to the remaining one 
            self.tail = new_node
        else:
            self.tail.next = new_node #else the tail.next is assigned to new_node
            self.tail = new_node # i guess its the same. tail  assigned to new_node
        self.length +=1
        return True
    
    # -----------------
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next



    # def getty(self,index):
    #     if index < 0 or index >= self.length:
    #         return None

    #     if index > self.length // 2:
    #         temp = self.tail
    #         for _ in range(self.length - index -1):
    #             if temp.prev is None:
    #                 return None
    #             temp = temp.prev
    #     else:
    #         temp = self.head
    #         for _ in range(index):
    #             if temp.next is None:
    #                 return None
    #             temp = temp.next

    #         return temp   

    # -----------------
  
    def pop_first(self,value): #remove first index from list
        if self.head is None: # this can self.length == 0 return None
            return False
        
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.length -=1
        return True 
    
    # def poppy_first(self,value):
    #     if self.length == 0:
    #         return None
        
    #     temp = self.head
    #     self.head = self.head.next

    #     temp.next = None
    #     self.length = None
    #     if self.length ==0:
    #         self.tail = None
    #     return temp

    # -----------------

    def pop_last(self,value): #pop -  Last in first out
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head

        #while (temp.next): is true
        while temp.next is not None and temp.value != value:
        #and temp.value != value:
            pre = temp 
            temp = temp.next 
        
        # if temp is None:
        #     return None
        
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


    def prepend(self,value): #sumpay sa first index sa list
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head #assign new_node to self.head
            self.head = new_node #point the NEW head node to new_node
        self.length += 1
        return True
    
       # -----------------
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
   
    def set_value1(self, index, value): #b3lat wa na mao!
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
        

# ----------------------------------

    def insert_value(self,index,value):
        if index < 0 or index >= self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        print("inserted {} at index {}".format(value,index))
        self.length +=1
        return True
    

# ----------------------------------

    def remove_value(self,index,value):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first
        if index == self.length -1:
            return self.pop_last
        
<<<<<<< HEAD
# ----------------------------------
    
=======
        # temp = self.index.value
        # prev = self.get(index - 1)

        # if temp:
        #     temp.next +=1
        # else
        
        else:
            current = self.head
            for _ in range(index -1):
              if current is None:
                raise IndexError("index out of range")
              current = current.next
            current.next = current.next.next
        print("removed {} at index {}".format(value,index))
        self.length +=1
        return True

>>>>>>> 8519313 (from room pc version)



    def remove_value(self,index):
        if index < 0 or index >= self.length:
            return None
        
        if index ==0:
            return self.pop_first()
        elif index == self.length -1:
            return self.pop_last()
        
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length = -1
        print("the removed index: {}".format(index))
       
        return temp

my_linked_list = LinkedList(10)
# print(my_linked_list.print_list())

# print("--running append func")
# my_linked_list.append(1)



# print("--running prepend(add item b4 index of List)")
# my_linked_list.prepend(0)
# my_linked_list.print_list()

# print("--running remove(remove 1st index sa list)")
# my_linked_list.pop_first(0)
# my_linked_list.print_list()

# print("--running pop() (ibta ang tail sa list)")
# my_linked_list.pop_last(2)
# my_linked_list.print_list()
<<<<<<< HEAD
print("--printing old list--")
my_linked_list.append(12)
my_linked_list.append(11)
my_linked_list.append(13)

=======
print("-- printing old list --")
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
>>>>>>> 8519313 (from room pc version)
my_linked_list.print_list()


# print("--running set value w/ loc as index val")
# my_linked_list.set_value1(1,66)

<<<<<<< HEAD
#my_linked_list.insert_value(1,1) // inserting something @ index
my_linked_list.remove_value(2)   # removing something at index
=======
#my_linked_list.insert_value(1,1)


my_linked_list.remove_value(2,2)
>>>>>>> 8519313 (from room pc version)
my_linked_list.print_list()

# print("--running get func")
# print(my_linked_list.get(2))
# my_linked_list.print_list()
# input("press enter to clear sceen")

# print('\033c', end='')
#print(my_linked_list.pop1())
#print(my_linked_list.pop1())
#print(my_linked_list.pop1())
#my_linked_list.print_list()




