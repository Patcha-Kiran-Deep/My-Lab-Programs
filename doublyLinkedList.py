

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:

    '''Operations on linked lists'''
    def __init__(self):
        self.header = None

    def takeInput(self):
        return eval(input("Enter the data : "))

    def getNode(self, position):
        currNode = self.header
        count = 1
        while position != count and currNode.next is not None:
            currNode = currNode.next
            count += 1
        return currNode


    # createNode defaults to insertion at the End of the linked list

    def createNode(self):
        newNode = Node(self.takeInput())
        if self.header == None:
            self.header = newNode
        else:
            lastNode = self.getNode(-1)
            lastNode.next = newNode
            newNode.prev = lastNode
            newNode.next = None
        

    def insertAtStart(self):
        newNode = Node(self.takeInput())
        if self.header == None:
            newNode.next = None
            newNode.prev = None
        else:
            newNode.prev = None
            newNode.next = self.header
            self.header.prev = newNode
        self.header = newNode


    def insertAtMiddle(self, pos):
        newNode = Node(self.takeInput())
        currNode = self.getNode(pos)
        newNode.next = currNode
        newNode.prev = currNode.prev
        currNode.prev.next = newNode
        currNode.prev = newNode


    def deleteAtStart(self):
        if self.header == None:
            print("No elements to delete")
        else:
            self.header.next.prev = Nonetail is the way to go, however in case for whatever reason you don't have tail, you can use tac + awk
        pass

    def deleteAtEnd(self):
        pass

    def traversalForward(self):
        currNode = self.header
        while currNode is not None:
            print(currNode.data)
            currNode = currNode.next

    def traversalReverse(self):
        pass

    def getValueAt(self, pos):
        pass
        






linkedList = DoublyLinkedList()


while True:
    print("Which operation you want to perform : ")
    choice = int(input("1. Creation\n2. Insertion\n3. Deletion\n4. Updation\n5. Display\n6. Obtain value\n7. Press any other key to exit\nEnter your choice : "))

    if choice == 1:
        linkedList.createNode()

    elif choice == 2:
        subChoice = int(input("1. Insert at start\n2. Insert at middle\n3. Insert at end : "))
        if subChoice == 1:
            linkedList.insertAtStart()
        elif subChoice == 2:
            position = int(input("At which node you want to insert the node : "))
            linkedList.insertAtMiddle(position)
        elif subChoice == 3:
            linkedList.createNode()
        else:
            print("Invalid Choice!")

    elif choice == 3:
        subChoice = int(input("1. Delete at start\n2. Delete at middle\n3. Delete at end : "))
        if subChoice == 1:
            linkedList.deleteAtStart()
        elif subChoice == 2:
            position = int(input("Position where you want to delete the node : "))
            linkedList.deleteAtMiddle(position)
        elif subChoice == 3:
            linkedList.deleteAtEnd()
        else:
            print("Invalid Choice!")

    elif choice == 4:
        position = int(input("Position where you want to update the node : "))
        linkedList.updateValueAt(position)

    elif choice == 5:
        subChoice = int(input("1. Forward Traversal\n2. Reverse Traversal : "))
        if subChoice == 1:
            linkedList.traversalForward()
        elif subChoice == 2:
            linkedList.traversalReverse

    elif choice == 6:
        position = int(input("Which node's data you want to fetch :"))
        linkedList.getValueAt(position)

    else:
        break
