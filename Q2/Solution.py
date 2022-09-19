class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def deleteNode(self, n):
        first = self.head
        second = self.head
        for i in range(n):
            if(second.next == None):
                if(i==n-1):
                    self.head = self.head.next
                return self.head
            second = second.next

        while(second.next!=None):
            second = second.next
            first = first.next
        first.next = first.next.next


    def printList(self):
        temp_head = self.head
        while(temp_head!=None):
            print(temp_head.data)
            temp_head=temp_head.next


listt = LinkedList()
listt.insert(1)
listt.insert(2)
listt.insert(3)
listt.insert(4)
listt.insert(5)
listt.printList()
listt.deleteNode(2)
print("-------")
listt.printList()

