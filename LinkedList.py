# Time: 2017/12/22 Theme: Linked List(unordered)  Pengfei Xiong
# Purpose: This is a simulation for linked list in python, in the simulation, we need to know:
#   1. Each node should have 2 attribute: one is its value, the other is the pointer to next value
#   2. Node should have method to get its value and pointer information, as well as set next node.

class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None

    def getvalue(self):
        return self.value

    def getnext(self):
        return self.next

    def setnext(self, next):
        self.next = next

    def setdata(self, data):
        self.value = data
    def deletenext(self):
        self.next = None

# After we create Node class, we need to start creating Linked list, it should have belowing attribute:
#   1. It should have head method, which give us the information what is the head.
#   2. isEmpty method to detect whether it's empty list.
#   3. add method to add item into linked list. For covenience, we add item in the front. 
#   4. size method to calculate the length of list.
#   5. search method to evaluate whether item is in the list.
#   6. remove method to remove item from the list.
class LinkedList(object):

    def __init__(self):
        self.head = None

    def __repr__(self):
        current = self.head
        str = ''
        count = 0
        while current:
            str = str + 'Link({0},'.format(current.value)
            count+=1
            current = current.getnext()
        str = str + 'nil'
        while count:
            str = str + ')'
            count-=1
        return str

    def isEmpty(self):
        return self.head == None

    # And item should be transfer into Node so that it can be Linked list.
    def add(self, item):
        temp =  Node(item)
        temp.setnext(self.head)     # Set current head to be the second, and item to be head.
        self.head = temp
        

    def size(self):
        count = 0
        current = self.head                    # 为了不改变self.head，我们必须先将它复制给另外的变量
        while current != None:
            current = current.getnext()
            count+=1
        return count

    def search(self,item):
        have = False
        current = self.head
        while current != None and have==False:
            if current.value == item:
                have = True
            else:
                current = current.getnext()
        return have

    # Remove method should have 2 functions:
    # 1. Judge whether item is in our linked list.
    # 2. If yes, remove that and return a new linked list.
    def remove(self,item):
        # We need to add in 2 more variables to help us finish this remove process: previous and current
        # Previous saves information of our previous item and current saves current information. If current 
        # equals to item, then we need to delete current and set previous connect to next item.
        previous = None
        current = self.head
        have = False
        while current.value != item and have == False:
            previous = current
            current = current.getnext()
            if current.value == item:
                have = True
        # If  item is the first one, we need this special process.
        if previous == None:
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext()) 

# Extra: create insert, index, pop, and append method in our linked list.
    def insert(self, item, position=0):
        previous = None
        current = self.head
        if position == 0:
            self.add(item)
        else:
            while position:
                previous = current
                current = current.getnext()
                position-=1
            temp = Node(item)
            temp.setnext(current)
            previous.setnext(temp)

    def index(self,item):
        have = False
        current = self.head
        count = 0
        while current != None and not have:
            if current.value == item:
                have = True
            current = current.getnext()
            count+=1
        if have:
            return count-1
        else:
            str = '{0} is not in the linked list'.format(item)
            return str

    def append(self, item):
        current = self.head
        previous = None
        temp = Node(item)
        while current != None:
            previous = current
            current = current.getnext()
        previous.setnext(temp)