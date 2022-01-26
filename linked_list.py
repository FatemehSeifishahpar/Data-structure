class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def insert(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
    
    def search(self,key):
        n=  self.head
        while n:
            if n.value == key:
                return True
            n=n.next
        return False

    def count(self,key):
        count = 0
        n = self.head
        while n:
            if n.value == key:
                count +=1
            n=n.next
        return count

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def remove(self,key):
        if self.isEmpty():
            return
        
        if self.head.value == key:
            n = self.head
            self.head = self.head.next
            del n
            print(f'{key} was removed')
            return

        n = self.head
        m = self.head.next

    
        while m != None:
            if m.value == key:
                n.next = m.next
                del m
                print(f'{key} was removed')
                break
            m = m.next
            n = n.next
            


    def traverse(self):
        n = self.head
        while n:
            print(n.value)
            n=n.next


link = LinkedList()
link.append(1)
link.insert(2)
link.append(3)
link.insert(4)
link.insert(4)
link.append(5)
link.traverse()
link.remove(4)
link.traverse()